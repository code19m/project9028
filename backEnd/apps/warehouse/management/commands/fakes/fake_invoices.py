input_invoices = [
    {
        # 1
        "supplier_id": 1,
        "status": "confirmed",
        "description": ""
    },
    {
        # 2
        "supplier_id": 2,
        "status": "confirmed",
        "description": ""
    },
    {
        # 3
        "supplier_id": 3,
        "status": "confirmed",
        "description": ""
    },
    {
        # 4
        "supplier_id": 1,
        "status": "confirmed",
        "description": ""
    },
    {
        # 5
        "supplier_id": 2,
        "status": "confirmed",
        "description": ""
    },
    {
        # 6
        "supplier_id": 3,
        "status": "new",
        "description": ""
    }
]

output_invoices = [
    {
        # 1
        "client_id": 1,
        "status": "confirmed",
        "description": ""
    },
    {
        # 2
        "client_id": 2,
        "status": "confirmed",
        "description": ""
    },
    {
        # 3
        "client_id": 3,
        "status": "new",
        "description": ""
    }
]

returned_invoices = [
    {
        "client_id": 3,
        "status": "confirmed",
        "description": ""
    },
    {
        "client_id": 2,
        "status": "confirmed",
        "description": ""
    }
]
