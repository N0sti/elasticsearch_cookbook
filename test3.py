# Recherche des index Suricata
def get_suricata_index():
    """Retourne le nom de l'index Suricata le plus récent"""
    try:
        indices = es.indices.get(index="suricata-*")
        if indices:
            return sorted(indices.keys())[-1]
    except:
        pass
    return "suricata-*"

index_name = get_suricata_index()

# Comptage des documents
try:
    count = es.count(index=index_name)
    print(f"Index: {index_name}")
    print(f"Nombre de documents: {count['count']:,}")
    
    # Exemple de document
    if count['count'] > 0:
        sample = es.search(index=index_name, size=1, query={"match_all": {}})
        if sample['hits']['hits']:
            doc = sample['hits']['hits'][0]['_source']
            print(f"\nExemple de document:")
            print(f"   Type: {doc.get('event_type', 'N/A')}")
            print(f"   Timestamp: {doc.get('@timestamp', doc.get('timestamp', 'N/A'))}")
            if 'src_ip' in doc:
                print(f"   Source: {doc.get('src_ip')}:{doc.get('src_port', 'N/A')}")
                print(f"   Destination: {doc.get('dest_ip')}:{doc.get('dest_port', 'N/A')}")
            if 'alert' in doc:
                alert = doc['alert']
                print(f"   Alerte: {alert.get('signature', 'N/A')}")
                print(f"   Sévérité: {alert.get('severity', 'N/A')}")
except Exception as e:
    print(f"Erreur: {e}")
