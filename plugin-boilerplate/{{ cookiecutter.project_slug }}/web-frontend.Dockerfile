FROM baserow/web-frontend:1.33.3

USER root

COPY ./plugins/{{ cookiecutter.project_module }}/ /baserow/plugins/{{ cookiecutter.project_module }}/
RUN /baserow/plugins/install_plugin.sh --folder /baserow/plugins/{{ cookiecutter.project_module }}

USER $UID:$GID
