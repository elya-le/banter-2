from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.models import db, Channel, Server
from app.forms.channel_form import ChannelForm

channel_routes = Blueprint('channels', __name__)

@channel_routes.route('/<int:server_id>', methods=['GET'])
@login_required
def get_channels(server_id):
    channels = Channel.query.filter_by(server_id=server_id).all()
    return jsonify([channel.to_dict() for channel in channels])

@channel_routes.route('/', methods=['POST'])
@login_required
def create_channel():
    form = ChannelForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        server = Server.query.get(form.data['server_id'])
        if server and server.creator_id == current_user.id:
            channel = Channel(
                name=form.data['name'],
                server_id=form.data['server_id']
            )
            db.session.add(channel)
            db.session.commit()
            return jsonify(channel.to_dict()), 201
        return {'error': 'Unauthorized or server not found'}, 403
    return {'errors': form.errors}, 400

@channel_routes.route('/<int:id>', methods=['GET'])
@login_required
def get_channel(id):
    channel = Channel.query.get(id)
    if channel:
        return jsonify(channel.to_dict())
    return {'error': 'Channel not found'}, 404

@channel_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_channel(id):
    channel = Channel.query.get(id)
    if channel:
        form = ChannelForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            server = Server.query.get(form.data['server_id'])
            if server and server.creator_id == current_user.id:
                channel.name = form.data['name']
                channel.server_id = form.data['server_id']  # make sure server_id is updated
                db.session.commit()
                return jsonify(channel.to_dict())
            return {'error': 'Unauthorized or server not found'}, 403
        return {'errors': form.errors}, 400
    return {'error': 'Channel not found'}, 404


@channel_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_channel(id):
    channel = Channel.query.get(id)
    if channel:
        server_id = channel.server_id  # save the server_id before deleting the channel
        server = Server.query.get(server_id)
        if server and server.creator_id == current_user.id:
            db.session.delete(channel)
            db.session.commit()
            return jsonify({'message': 'Channel deleted', 'server_id': server_id}), 200  # Return server_id
        return {'error': 'Unauthorized'}, 403
    return {'error': 'Channel not found'}, 404

