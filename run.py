import os
from src.server.server import create_app
from src.models.users import Users
from src.models.token_block_list import TokenBlockList

app = create_app(os.getenv('CONFIG_MODE'))

if __name__ == '__main__':
    print("Running app")
    app.run(host='0.0.0.0', port=3000, debug=True)