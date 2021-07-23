def create_classes(db):
    
    # Class needed for each table
    class Tv_watched(db.Model):
        __tablename__ = 'tv_watched'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        hours = db.Column(db.Float)

        def __repr__(self):
            return '<TV Watched %r>' % (self.name)
    return Tv_watched

def create_tv_watched_geo(db):

    class Tv_watched_geo(db.Model):
        __tablename__ = 'tv_watched_geo'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50))
        hours = db.Column(db.Float)
        lat = db.Column(db.Float)
        lon = db.Column(db.Float)

        def __repr__(self):
            return '<TV Watched %r>' % (self.name)
    return Tv_watched_geo