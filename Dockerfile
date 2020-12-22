FROM python:3
COPY moodle_plugin_version_generator.py /moodle_plugin_version_generator.py
CMD ["python", "/moodle_plugin_version_generator.py"]