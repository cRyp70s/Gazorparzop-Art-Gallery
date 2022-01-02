from flask import render_template, request, abort, jsonify

# from marshmallow import Schema, fields

from .models import GalleryEntry
from . import app


@app.route("/collections")
def collections():
    args = request.args
    search = args.get("s", "", str)
    page = args.get("p", 1, int)
    order_by = args.get("sort", "alpha", str)
    col = args.get("coll", "", str)
    order = {
        "alpha": GalleryEntry.title,
        "collection": GalleryEntry.collection,
        "created": GalleryEntry.created,
    }

    result = GalleryEntry.query
    if col and col.lower() != "all":
        result = result.filter_by(collection=col)
    # result = result.search(s)
    ord_ = order.get(order_by)
    if ord_:
        asc_desc = {"asc": ord_.asc(), "desc": ord_.desc()}
        result = result.order_by(asc_desc.get(args.get("asc_desc"), asc_desc["desc"]))
    paginate = result.paginate(page, per_page=6, error_out=False)
    if page > paginate.pages:
        abort(404)
    return render_template(
        "collections.html", result=paginate, col=col, order=order_by, s=search
    )


@app.route("/get-item/<int:id>")
def get_item(id):
    item = GalleryEntry.query.filter_by(id=id).first_or_404()
    out = {
        "img_src": item.sample_img_url,
        "title": item.title,
        "descr": item.description,
        "artist": item.artist,
        "collection": item.collection,
        "created": item.created,
    }
    return jsonify(out)
