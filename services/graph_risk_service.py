from graph.neo4j_client import neo4j_client


def check_graph_risks(sender, receiver):

    return {

        "shared_device":
            neo4j_client.check_shared_device(sender),

        "circular_flow":
            neo4j_client.check_circular_flow(sender),

        "mule_account":
            neo4j_client.check_mule_account(receiver)
    }