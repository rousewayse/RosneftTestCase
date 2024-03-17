from os import environ


environ.setdefault('DB', 'pony')
environ.setdefault('DB_USER', 'postgres')
environ.setdefault('DB_PASS', 'x')
environ.setdefault('DB_PORT', '5432')
environ.setdefault('DB_HOST', 'localhost')

bind_config = {
        'provider': 'postgres',
        'host': environ.get('DB_HOST'),
        'user': environ.get('DB_USER'),
        'database': environ.get('DB'),
        'password': environ.get('DB_PASS'),
        'port': environ.get('DB_PORT')
     }

generate_mapping_config = {
        "create_tables": True
    }
