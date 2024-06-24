import json
from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Info:
    activity_days: int
    activity_type: int
    end_time: int
    entry_img: str
    is_hot: bool
    join_end_time: int
    promotion_id: int
    require_count: int
    reward_count: int
    reward_type: int
    rule_desc: str
    start_time: int
    status: int
    title: str

    @staticmethod
    def from_dict(obj: Any) -> 'Info':
        assert isinstance(obj, dict)
        activity_days = from_int(obj.get("activity_days"))
        activity_type = from_int(obj.get("activity_type"))
        end_time = from_int(obj.get("end_time"))
        entry_img = from_str(obj.get("entry_img"))
        is_hot = from_bool(obj.get("is_hot"))
        join_end_time = from_int(obj.get("join_end_time"))
        promotion_id = from_int(obj.get("promotion_id"))
        require_count = from_int(obj.get("require_count"))
        reward_count = from_int(obj.get("reward_count"))
        reward_type = from_int(obj.get("reward_type"))
        rule_desc = from_str(obj.get("rule_desc"))
        start_time = from_int(obj.get("start_time"))
        status = from_int(obj.get("status"))
        title = from_str(obj.get("title"))
        return Info(activity_days, activity_type, end_time, entry_img, is_hot, join_end_time, promotion_id, require_count, reward_count, reward_type, rule_desc, start_time, status, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["activity_days"] = from_int(self.activity_days)
        result["activity_type"] = from_int(self.activity_type)
        result["end_time"] = from_int(self.end_time)
        result["entry_img"] = from_str(self.entry_img)
        result["is_hot"] = from_bool(self.is_hot)
        result["join_end_time"] = from_int(self.join_end_time)
        result["promotion_id"] = from_int(self.promotion_id)
        result["require_count"] = from_int(self.require_count)
        result["reward_count"] = from_int(self.reward_count)
        result["reward_type"] = from_int(self.reward_type)
        result["rule_desc"] = from_str(self.rule_desc)
        result["start_time"] = from_int(self.start_time)
        result["status"] = from_int(self.status)
        result["title"] = from_str(self.title)
        return result


@dataclass
class Request:
    info: Info

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        assert isinstance(obj, dict)
        info = Info.from_dict(obj.get("info"))
        return Request(info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["info"] = to_class(Info, self.info)
        return result


def request_from_dict(s: Any) -> Request:
    return Request.from_dict(s)


def request_to_dict(x: Request) -> Any:
    return to_class(Request, x)


if __name__ == '__main__':


    # 给定的 JSON 数据
    json_data = '''
    {
        "info": {
            "admin_id": 1,
            "status": 2,
            "title": "测试下单挑战赛",
            "entry_img": "https://img.dac6.cn/uploads/images/20240223/202402231103474c3935507.png",
            "activity_days": 1,
            "activity_type": 1,
            "require_count": 1,
            "reward_count": 1,
            "reward_type": 1,
            "rule_desc": "<p>测试推荐</p>",
            "start_time": 1709136000,
            "end_time": 1709913599,
            "join_end_time": 1709740798,
            "is_hot": false,
            "share_image": "",
            "share_txt": "",
            "share_desc": "",
            "order_require_type": 2,
            "register_count": 0
        }
    }
    '''

    # 将 JSON 数据解析为字典
    data_dict = json.loads(json_data)

    # 获取 "info" 字段
    info_data = data_dict.get("info", {})

    # 检查不符合字段
    invalid_fields = [key for key in info_data.keys() if key not in Info.__annotations__]
    print("不符合字段:", invalid_fields)

