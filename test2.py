# Vérification des services Docker
services = ['es01', 'es02', 'es03', 'kibana', 'suricata', 'filebeat']
running = []

for service in services:
    try:
        result = subprocess.run(
            ['docker', 'ps', '--filter', f'name={service}', '--format', '{{.Names}}'],
            capture_output=True, text=True, timeout=5
        )
        if service in result.stdout:
            running.append(service)
            print(f"Oko {service}")
        else:
            print(f"Not oko {service}")
    except:
        print(f"Not oko {service}")

if len(running) == len(services):
    print(f"\nTous les services sont démarrés ({len(running)}/{len(services)})")
else:
    print(f"\nServices démarrés: {len(running)}/{len(services)}")