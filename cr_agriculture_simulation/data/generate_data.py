def generate_random_data(n=100):
    cluster_id = np.random.choice(['A','B','C','D'], n)
    signal_strength = np.random.uniform(-90, -30, n)
    node_status = np.random.choice(['Active','Idle','Fault'], n)
    energy_consumption = np.random.uniform(200, 700, n)
    ...
    df['cluster_id'] = cluster_id
    df['signal_strength'] = signal_strength
    df['node_status'] = node_status
    df['energy_consumption'] = energy_consumption
    ...
