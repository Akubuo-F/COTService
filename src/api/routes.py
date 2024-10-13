from fastapi import APIRouter
from fastapi.responses import JSONResponse

api_routes = APIRouter()


@api_routes.get("/cot_service/reports/latest-report")
async def get_latest_report():
    return JSONResponse(
        status_code=200,
        content={
            "contract_name": "",
            "open_interest": {
                "total": 0,
                "speculators": {
                    "ratio": 0.00,
                    "change": 0
                },
                "hedgers": {
                    "ratio": 0.00,
                    "change": 0
                }
            },
            "noncommercial_positions": {
                "long": 0,
                "short": 0,
                "open_interest": 0,
                "long_ratio": 0.00,
                "short_ratio": 0.00,
                "change_in_long": 0,
                "change_in_short": 0,
                "net_position": 0
            },
            "commercial_positions": {
                "long": 0,
                "short": 0,
                "open_interest": 0,
                "long_ratio": 0.00,
                "short_ratio": 0.00,
                "change_in_long": 0,
                "change_in_short": 0,
                "net_position": 0
            },
            "net_positions": {
                "total": 0,
                "commercial": 0,
                "noncommercial": 0
            },
            "historical_comparisons": {
                "previous_week": {
                    "noncommercial": {
                        "long": 0,
                        "short": 0
                    },
                    "commercial": {
                        "long": 0,
                        "short": 0
                    }
                },
                "historical_average": {
                    "noncommercial": {
                        "long": 0,
                        "short": 0
                    },
                    "commercial": {
                        "long": 0,
                        "short": 0
                    }
                }
            },
            "market_sentiment": {
                "extreme_long_positions": False,
                "extreme_short_positions": False
            }
        }
    )