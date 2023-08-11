import json
import pytest

from task_1 import Project, User, UserNotFoundError


@pytest.fixture
def temp_file(tmp_path):
    t_name = tmp_path / 'task2.json'
    with open(t_name, 'w', encoding='utf-8') as f:
        data = {
            "1": {"02": "Tom", },
            "2": {"02": "Bill", },
            "3": {
                "03": "Roy",
            }
        }

        json.dump(data, f, ensure_ascii=True)
    yield t_name


@pytest.fixture
def get_users(temp_file):
    proj = Project.load_js(temp_file)
    return proj


@pytest.mark.parametrize("name, id_, result",
                         [
                             ("Bill", 2, User("Bill", 2)),
                             ("Roy", 5, "User Roy 5 not found! Access denied!!!"),
                         ]
                         )
def test_enter(name, id_, result, get_users):
    if isinstance(result, User):
        get_users.enter(name, id_)
        assert get_users.u_admin == result
    else:
        with pytest.raises(UserNotFoundError) as exc_info:
            get_users.enter(name, id_)
        assert str(exc_info.value) == result


@pytest.mark.parametrize("first_user, second_user, exp",
                         [
                             (User("Tom", '01'), User("Tom", '01'), True),
                             (User("Tom", '02'), User("Tom", '01'), False),
                         ])
def test_users(first_user, second_user, exp):
    assert (first_user == second_user) == exp


if __name__ == "__main__":
    pytest.main(["-v"])

