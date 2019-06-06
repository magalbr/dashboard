
import flask
import requests


blueprint = flask.Blueprint('gitlab', __name__)

ACCESS_TOKEN = 'ApP7jxoeh_qGepmysaBs'

PROJECTS_URL = 'https://gitlab.com/api/v4/projects?owned=true&private_token={}'.format(ACCESS_TOKEN)
ID='12680395'

PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/{}/repository/commits?private_token={}'.format(ID,ACCESS_TOKEN)
CREATE_PROJECT_URL = 'https://gitlab.com/api/v4/projects/user/{}'
PROJECT_ID = 'https://gitlab.com/projects/{}'


@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():
    
    context = {
        'page': 'gitlab',
        'projects': requests.get(PROJECTS_URL).json(),
        
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<int:projectid>', methods=[ 'GET' ])
def get_project_commits(projectid):

    PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/' + str(projectid) + '/repository/commits?private_token={}'.format(ACCESS_TOKEN)

    context = {
        'page': 'commits',
        'commits': requests.get(PROJECT_COMMITS).json(),
    }

    return flask.render_template('commits.html', context=context)

# @blueprint.route('/gitlab/<int:projectid>', methods=[ 'GET' ])
# def get_gitlab():
    
#         context = {
#         'page': 'gitlab',
#         'projects': requests.get(PROJECT_ID).json(),
                
#     }

#     

