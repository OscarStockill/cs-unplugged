import os.path
from utils.BaseLoader import BaseLoader
from topics.models import CurriculumArea


class FollowUpActivitiesLoader(BaseLoader):
    """Loader for follow up activites"""

    def __init__(self, load_log, structure_file, topic, BASE_PATH):
        """Initiates the loader for follow up activites

        Args:
            structure_file: file path (string)
            topic: Topic model object
        """
        super().__init__(BASE_PATH, load_log)
        self.structure_file = os.path.join(self.BASE_PATH, structure_file)
        self.BASE_PATH = os.path.join(self.BASE_PATH, os.path.split(structure_file)[0])
        self.topic = topic

    def load(self):
        """Load the content for follow up activities"""
        if self.structure_file:
            structure = self.load_yaml_file(self.structure_file)

            for activity_slug, activity_data in structure.items():
                md_file = activity_data['md-file']
                activity_content = self.convert_md_file(os.path.join(self.BASE_PATH, md_file))

                activity = self.topic.topic_follow_up_activities.create(
                    slug=activity_slug,
                    number=activity_data['number'],
                    name=activity_content.title,
                    content=activity_content.html_string,
                )
                activity.save()

                # Add curriculum areas
                curriculum_area_slugs = activity_data['curriculum-areas']
                for curriculum_area_slug in curriculum_area_slugs:
                    curriculum_area = CurriculumArea.objects.get(
                        slug=curriculum_area_slug
                    )
                    activity.curriculum_areas.add(curriculum_area)

                self.log('Added Activity: {}'.format(activity.name), 1)
