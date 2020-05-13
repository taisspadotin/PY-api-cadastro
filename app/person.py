from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from .model import Person
from .serealizer import PersonSchema


bp_person = Blueprint('person', __name__)


@bp_person.route('/mostrar', methods=['GET'])
#@jwt_required
def mostrar():
    result = Person.query.all()
    return PersonSchema(many=True).jsonify(result), 200


@bp_person.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Person.query.filter(Person.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_person.route('/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = PersonSchema()
    query = Person.query.filter(Person.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_person.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = PersonSchema()
    person, error = bs.load(request.json)

    if error:
        return jsonify(error), 401

    current_app.db.session.add(person)
    current_app.db.session.commit()
    return bs.jsonify(person), 201
