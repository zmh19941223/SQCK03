# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcase\测试开发3_abc.json


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCase测试开发3Abc(HttpRunner):

    config = Config("abc").base_url("http://localhost")

    teststeps = [
        Step(RunRequest("step_name").get("/demo/path")),
    ]


if __name__ == "__main__":
    TestCase测试开发3Abc().test_start()
