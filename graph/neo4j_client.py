from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()


class Neo4jClient:

    def __init__(self):

        # self.driver = GraphDatabase.driver(
        #     os.getenv("NEO4J_URI"),
        #     auth=(
        #         os.getenv("NEO4J_USER"),
        #         os.getenv("NEO4J_PASSWORD")
        #     )
        # )
        uri = ""
        user = ""
        password = ""

        self.driver = GraphDatabase.driver(
            uri,
            auth=(user, password)
        )

    
    def create_customer(self, name, country, kyc_status):

        query = """
        MERGE (c:Customer {name:$name})

        SET c.country=$country,
            c.kyc_status=$kyc_status
        """

        with self.driver.session() as session:
            session.run(
                query,
                name=name,
                country=country,
                kyc_status=kyc_status
            )

    
    #LINK CUSTOMER TO DEVICE
    def link_device(self, customer, device_id):

        query = """
        MERGE (c:Customer {name:$customer})

        MERGE (d:Device {device_id:$device_id})

        MERGE (c)-[:USES]->(d)
        """

        with self.driver.session() as session:
            session.run(
                query,
                customer=customer,
                device_id=device_id
            )

    #########################################################
    # CREATE TRANSACTION
    #########################################################

    def create_transaction(
        self,
        txn_id,
        sender,
        receiver,
        amount,
        country,
        device_id,
        ip_address,
        bank_account
    ):

        query = """
        MERGE (s:Customer {name:$sender})
        MERGE (r:Customer {name:$receiver})

        MERGE (d:Device {device_id:$device_id})
        MERGE (ip:IPAddress {address:$ip_address})
        MERGE (b:BankAccount {account_no:$bank_account})

        MERGE (s)-[:USES]->(d)
        MERGE (s)-[:USES_IP]->(ip)
        MERGE (s)-[:OWNS]->(b)

        CREATE (t:Transaction {
            txn_id:$txn_id,
            amount:$amount,
            country:$country
        })

        MERGE (s)-[:SENT]->(t)
        MERGE (t)-[:RECEIVED_BY]->(r)
        """

        with self.driver.session() as session:

            session.run(
                query,
                txn_id=txn_id,
                sender=sender,
                receiver=receiver,
                amount=amount,
                country=country,
                device_id=device_id,
                ip_address=ip_address,
                bank_account=bank_account
            )

    #########################################################
    # SHARED DEVICE
    #########################################################

    def check_shared_device(self, customer):

        query = """
        MATCH (c1:Customer {name:$customer})
              -[:USES]->
              (d:Device)
              <-[:USES]-
              (c2:Customer)

        WHERE c1 <> c2

        RETURN
            count(c2) AS cnt,
            d.device_id AS device,
            collect(c2.name) AS customers
        """

        with self.driver.session() as session:

            record = session.run(
                query,
                customer=customer
            ).single()

            if record is None:

                return {
                    "detected": False,
                    "device_id": None,
                    "other_customers": []
                }

            if record["cnt"] == 0:

                return {
                    "detected": False,
                    "device_id": None,
                    "other_customers": []
                }

            return {
                "detected": True,
                "device_id": record["device"],
                "other_customers": record["customers"]
            }

    #########################################################
    # CIRCULAR FLOW
    #########################################################

    def check_circular_flow(self, customer):

        query = """
        MATCH p=
        (c:Customer {name:$customer})
        -[:SENT]->
        (:Transaction)
        -[:RECEIVED_BY]->
        (:Customer)
        -[:SENT]->
        (:Transaction)
        -[:RECEIVED_BY]->
        (c)

        RETURN count(p) AS cnt
        """

        with self.driver.session() as session:

            record = session.run(
                query,
                customer=customer
            ).single()

            if record is None:
                return {
                    "detected": False,
                    "cycle_count": 0
                }

            return {
                "detected": record["cnt"] > 0,
                "cycle_count": record["cnt"]
            }

    #########################################################
    # MULE ACCOUNT
    #########################################################

    def check_mule_account(self, receiver):

        query = """
        MATCH (s:Customer)
              -[:SENT]->
              (:Transaction)
              -[:RECEIVED_BY]->
              (r:Customer {name:$receiver})

        RETURN count(s) AS cnt
        """

        with self.driver.session() as session:

            record = session.run(
                query,
                receiver=receiver
            ).single()

            if record is None:
                return {
                    "detected": False,
                    "incoming_senders": 0
                }

            return {
                "detected": record["cnt"] >= 5,
                "incoming_senders": record["cnt"]
            }

    #########################################################
    # CONNECTION TEST
    #########################################################

    def test_connection(self):

        with self.driver.session() as session:

            result = session.run(
                "RETURN 'Neo4j Connected' AS msg"
            )

            return result.single()["msg"]


neo4j_client = Neo4jClient()