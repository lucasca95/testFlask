from . import db

class Firmware(db.Model):
    """Model for user accounts."""

    __tablename__ = 'firmwares'
    id = db.Column(db.Integer,
                   primary_key=True)
    tipoPlaca = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    versionFirmware = db.Column(db.String(11),
                      index=True,
                      unique=False,
                      nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)

    #def __repr__(self):
    #    return '<firmware {}>'.format(self.tipoPlaca+self.versionFirmware)