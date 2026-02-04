import requests
import pandas as pd
import time
from requests.exceptions import ReadTimeout, RequestException

API_URL = "https://openatom.tech/api/user/v1/un/eventList"

# ⚠️ 直接从浏览器复制 Cookie（最简单 & 稳定）
COOKIE = "atom_user={%22id%22:%22649a75c5d30b2b0d3de9086e%22%2C%22username%22:%22tianchang%22%2C%22nickname%22:%22tianchang%22%2C%22photo%22:%22/uploads/user/1698197408152_6706.jpeg%22%2C%22userNameSpace%22:%22tianchang%22%2C%22phone%22:%2218539162972%22%2C%22phoneVerified%22:true%2C%22email%22:%22xuchenyang@openatom.org%22%2C%22emailVerified%22:true%2C%22adminRoleCode%22:null}; ak_user_locale=zh_CN; teambition_lang=zh_CN; Hm_lvt_3aae7019e3354d0d43daf0842ea3d4b2=1766633341,1767080796; HMACCOUNT=682844590C5FAD81; ATOMGIT_ID_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2NDlhNzVjNWQzMGIyYjBkM2RlOTA4NmUiLCJhdWQiOiI2MmQ3YTBlYmFmOTViZGFjZjc0ZmM2YjkiLCJpYXQiOjE3Njc4NTk0NzYsImV4cCI6MTc2OTA2OTA3NiwiaXNzIjoiaHR0cHM6Ly9wYXNzcG9ydC5vcGVuYXRvbS50ZWNoL29pZGMiLCJub25jZSI6Ikk2OWtLRDM5RksiLCJuYW1lIjpudWxsLCJnaXZlbl9uYW1lIjpudWxsLCJtaWRkbGVfbmFtZSI6bnVsbCwiZmFtaWx5X25hbWUiOm51bGwsIm5pY2tuYW1lIjoidGlhbmNoYW5nIiwicHJlZmVycmVkX3VzZXJuYW1lIjpudWxsLCJwcm9maWxlIjoi5YmN56uv5LmL6JmO77yI5oGp5biIIGhleC1jae-8iVxuIiwicGljdHVyZSI6Ii8vc3RhdGljLm9wZW5hdG9tLnRlY2gvc3RhdGljcy9hdXRoaW5nLWNvbnNvbGUvL3VwbG9hZHMvdXNlci8xNjk4MTk3NDA4MTUyXzY3MDYuanBlZyIsIndlYnNpdGUiOiJodHRwczovL3RpYW5jaGFuZy5hdG9tZ2l0Lm5ldC9vcGVuYXRvbS1SLUQtRGVwYXJ0bWVudC1ib29rLyIsImJpcnRoZGF0ZSI6bnVsbCwiZ2VuZGVyIjoiVSIsInpvbmVpbmZvIjpudWxsLCJsb2NhbGUiOm51bGwsInVwZGF0ZWRfYXQiOiIyMDI2LTAxLTA4VDA4OjA0OjM0LjYxMVoiLCJlbWFpbCI6Inh1Y2hlbnlhbmdAb3BlbmF0b20ub3JnIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX251bWJlciI6IjE4NTM5MTYyOTcyIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjp0cnVlfQ.llTyPjQ8V-tZi7R1AEZ6LXQyDyK6MlhilgQjJkRaCcA; ATOMGIT_ACCESS_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlBTRkpTbFhZTGphbFA4RGZpUTZITk53TkFXM0FkT1dscTFKaVpTMmlkbFUifQ.eyJzdWIiOiI2NDlhNzVjNWQzMGIyYjBkM2RlOTA4NmUiLCJhdWQiOiI2MmQ3YTBlYmFmOTViZGFjZjc0ZmM2YjkiLCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwaG9uZSBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIiwiaWF0IjoxNzY3ODU5NDc2LCJleHAiOjE3NjkwNjkwNzYsImp0aSI6IlVzNHUtc0tYc1VLcUZZM1dROFFFcXlFd3c1RVVjLXVydzVjOU5vNVktdVAiLCJpc3MiOiJodHRwczovL3Bhc3Nwb3J0Lm9wZW5hdG9tLnRlY2gvb2lkYyJ9.UdOWsGVYFYf7aBzGfGyd1g_GgNDq2gBptkNyTG6_VxMEmPou9Du01bLeaHZ6wD_EL9g8LOaS2BqOlQ4lySZU3rlUbbvQb3sq4p0VAHfb3vr5qI6cV1erJnjBltLHQJgRzein_ClexrBXKrsvRKJPDmrxLt_bxjheUE370yrxbomWACGsCgnndpScCkpUJ8iL-hz8enO_1fPU3ZfgY3H3DwxMeoOY_c_diXrfPbZfp1Iebi4S5iqdi6Rjq7Dez1iKhR-Yw4dWJe18fhe_FdjpWbGVsqNpmuJ-IR8ns8ZIOKrNXXfVA7drX_VyrRUm3MInQ6tH8SAgqYcnZolVeN1e8A; ATOMGIT_REFRESH_TOKEN=JzagZ7hfWViClvwsWAeY7WRQwXwCn-3UiDCbfe5Xl0L; ATOMGIT_EXPIRES_IN=1209600; ATOMGIT_EXPIRES_AT=1769069076; DEFAULT_LANG=zh_CN; Hm_lpvt_3aae7019e3354d0d43daf0842ea3d4b2=1768273977"

HEADERS = {
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://openatom.tech",
    "referer": "https://openatom.tech/tianchang?year=2025",
    "user-agent": "Mozilla/5.0",
    "cookie": COOKIE,
}

PAYLOAD_BASE = {
    "start": "2025-01-01 00:00:00",
    "end": "2025-12-31 23:59:59",
    "pageSize": 20,
    "externUid":"tianchang"
}

def fetch_all_events():
    page = 1
    all_items = []
    max_retries = 3

    while True:
        payload = {
            **PAYLOAD_BASE,
            "page": page,
        }

        for attempt in range(1, max_retries + 1):
            try:
                resp = requests.post(
                    API_URL,
                    headers=HEADERS,
                    json=payload,
                    timeout=30  # ⬅️ 拉长
                )
                resp.raise_for_status()
                result = resp.json()
                break
            except ReadTimeout:
                print(f"⏱ Page {page} 超时，第 {attempt} 次重试")
                time.sleep(2 * attempt)
            except RequestException as e:
                print(f"❌ Page {page} 请求失败: {e}")
                return all_items
        else:
            print(f"🚫 Page {page} 多次失败，跳过")
            page += 1
            continue

        date_map = result.get("dateMap", {})
        print(f"📄 Page {page}, days: {len(date_map)}")

        if not date_map:
            break

        for date, events in date_map.items():
            for event in events:
                event["event_date"] = date
                all_items.append(event)

        if page >= result.get("totalPage", 0):
            break

        page += 1
        time.sleep(0.5)  # ⬅️ 主动放慢

    return all_items


def export_csv(items, filename="openatom_events_2025.csv"):
    if not items:
        print("⚠️ 没有数据可导出")
        return

    df = pd.DataFrame(items)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"✅ 已导出 {len(df)} 条数据 -> {filename}")


if __name__ == "__main__":
    events = fetch_all_events()
    export_csv(events)