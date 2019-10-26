from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Firmware

@app.route('/', methods=['GET'])
def create_user():
    """Create a user."""
    placa = request.args.get('placa')
    v_firm = request.args.get('vfirm')
    if placa and v_firm:
        ya_existe = Firmware.query.filter(Firmware.tipoPlaca == placa or Firmware.versionFirmware == v_firm).first()
        if ya_existe:
            return make_response(f'{placa} ({v_firm}) already created!')
        new_firm = Firmware(tipoPlaca=placa,
                        versionFirmware=v_firm,
                        created=dt.now())
        db.session.add(new_firm)  # Adds new Firmware record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{new_firm} successfully created!")