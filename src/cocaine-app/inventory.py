from config import config
from importer import import_object


try:
    inv = import_object(config['inventory'])
except (ImportError, KeyError):
    import fake_inventory as inv

get_dc_by_host = inv.get_dc_by_host
get_host_tree = inv.get_host_tree
node_shutdown_command = inv.node_shutdown_command
node_start_command = inv.node_start_command
node_reconfigure = inv.node_reconfigure
get_balancer_node_types = inv.get_balancer_node_types
get_dc_node_type = inv.get_dc_node_type
set_net_monitoring_downtime = inv.set_net_monitoring_downtime
remove_net_monitoring_downtime = inv.remove_net_monitoring_downtime
get_host_ip_addresses = inv.get_host_ip_addresses
get_new_group_files = inv.get_new_group_files
get_node_config_path = inv.get_node_config_path
get_node_types = inv.get_node_types
