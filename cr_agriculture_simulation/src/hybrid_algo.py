def cso_fba_optimization(df):
    # Simulate CSO: spider-based grouping
    df['selected_spider_group'] = ((df['temperature'] > 30) & (df['soil_moisture'] < 400)).astype(int)
    # Simulate FBA: optimal cluster and resource assignment
    df['optimal_cluster'] = df['cluster_id'].apply(lambda x: 'Optimal' if x in ['A', 'C'] else 'Suboptimal')
    # Decision: recommended action
    df['action'] = ['Irrigate' if sm < 400 else 'Skip' for sm in df['soil_moisture']]
    return df
