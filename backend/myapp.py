import os

from app import app, db
from app.models import GalleryEntry
from app.views import *

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "XSFDfvbdierhu4erhuf9re0ri409fdbvnhkvdbc djcffd./scd3"
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
