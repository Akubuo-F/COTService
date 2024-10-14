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
                "speculators": 0,
                "hedgers": 0
            },
            "changes": {
                "open_interest": {
                    "total": 0,
                    "speculators": 0,
                    "hedgers": 0
                },
                "traders_positions": {
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
            "positions": {
                "noncommercial_long": 0,
                "noncommercial_short": 0,
                "commercial_long": 0,
                "commercial_short": 0,
                "net": 0,
                "net_commercial": 0,
                "net_noncommercial": 0
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
                        "long": 0.00,
                        "short": 0.00
                    },
                    "commercial": {
                        "long": 0.00,
                        "short": 0.00
                    }
                }
            },
            "market_sentiment": {
                "extreme_long_positions": False,
                "extreme_short_positions": False
            }
        }
    )