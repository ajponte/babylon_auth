"""Instantiate a dev server."""
import uvicorn
from auth_server.app import create_app

def main():
    # app = create_app()
    uvicorn.run("auth_server.app:create_app", factory=True, reload=True)


if __name__ == '__main__':
    main()
