from django.test.simple import DjangoTestSuiteRunner

class DiscoveryRunner(DjangoTestSuiteRunner):
    """A test suite runner using unittest2 discovery."""
    def build_suite(self, test_labels):

        suite = None
        discovery_root = settings.TEST_DISCOVERY_ROOT

        if test_labels:
            suite = defaultTestLoader.loadTestsFromNames(
                test_labels)

        if suite is None:
            suite = defaultTestLoader.discover(
                discovery_root,
                top_level_dir=settings.BASE_PATH,
                )

        return reorder_suite(suite, (TestCase,))
