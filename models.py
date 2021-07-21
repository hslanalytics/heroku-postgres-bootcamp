def create_classes(db):
    class Tv_watched(db.Model):
        __tablename__ = 'tv_watched'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        hours = db.Column(db.Float)

        def __repr__(self):
            return '<TV Watched %r>' % (self.name)
    return Tv_watched
