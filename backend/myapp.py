import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from app.models import GalleryEntry
from app.views import *

admin = Admin(name="microblog", template_mode="bootstrap4")
admin.add_view(ModelView(GalleryEntry, db.session))
admin.init_app(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY) or "XSFDfvbdierhu4erhuf9re0ri409fdbvnhkvdbc djcffd./scd3"
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
