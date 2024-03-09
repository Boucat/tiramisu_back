SECRET_KEY = '9f44fd3304e0a7d0832f0627d9f9c6066a47786551a346bc47225eb65549d257'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


USER_MOCK_DB = {
    'ferrannoguera': {
        'username': 'ferrannoguera',
        'full_name': 'Ferran Noguera',
        'description': 'Parla de tiramisus i et diré quantes culleretes calces. (Spoiler: No més de 6)',
        'photo_url': 'https://raw.githubusercontent.com/Boucat/tiramisu_back/main/media/users/ferrannoguera.jpg',
        'hashed_password': '$2b$12$t4WQiOBSux.0UtPxcC19qOpPwmZ1yr.d1W80OD7Qy.jBJzyYDRk1q',
        'disabled': False,
    },
    'marcklingenberg': {
        'username': 'marcklingenberg',
        'full_name': 'Marc Klingenberg',
        'description': 'Amb llicència per degustar tiramisú',
        'photo_url': 'https://raw.githubusercontent.com/Boucat/tiramisu_back/main/media/users/marcklingenberg.jpg',
        'hashed_password': '$2b$12$pyjm6OllSwySLr4eFEPcWePYRsDtkt7Rwv6z2WzzCiiv84nJVesSa',
        'disabled': False,
    },
    'albertsuarez': {
        'username': 'albertsuarez',
        'full_name': 'Albert Suarez',
        'description': 'A punt de tastar el pitjor tiramisú georgiano de la història',
        'photo_url': 'https://raw.githubusercontent.com/Boucat/tiramisu_back/main/media/users/albertsuarez.jpg',
        'hashed_password': '$2b$12$wL.IHscc0M7cKgBX/mGbbejCUQPKD0KDmrwbTAdi1rNxHSj8XPvGm',
        'disabled': False,
    },
}

__all__ = [
    'SECRET_KEY',
    'ALGORITHM',
    'ACCESS_TOKEN_EXPIRE_MINUTES',
    'USER_MOCK_DB',
]
