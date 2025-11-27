from fastapi import APIRouter

router = APIRouter(prefix="/stores", tags=["stores"])

# Sample in-memory store data with closed_date (two are null)
stores_db = {
    "01234": {"store_id": "01234", "name": "Main Street Store", "closed_date": "2024-12-31"},
        "56789": {"store_id": "56789", "name": "Mall Store", "closed_date": "2025-06-30"},
            "11111": {"store_id": "11111", "name": "Airport Store", "closed_date": None},
                "22222": {"store_id": "22222", "name": "Suburban Store", "closed_date": None},
                    "33333": {"store_id": "33333", "name": "Beachfront Store", "closed_date": "2027-03-20"},
                    }

                    # Return the whole list of stores
                    @router.get("/")
                    def list_stores():
                        return {"resource": "stores", "stores": list(stores_db.values())}