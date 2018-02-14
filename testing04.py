import unittest

from homework04 import getUserRepos
from homework04 import getTotalCommits


class TestGitRepo(unittest.TestCase):
    def testRepo(self):
        self.assertEqual(getUserRepos('CelesteSakhile'), ['GitHubApi567','Triangle567'], 'The repositories for user CelesteSakhile'
                                                                                         ' are GitHubApi567 and Triangle567')

    def testRepoCommitCount(self):
        self.assertEqual(getTotalCommits('CelesteSakhile', 'Triangle567'), 7, 'The total number of commits for repository Triangle567 are 7')

if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()