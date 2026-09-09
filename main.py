from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import Annotated

from fastapi.staticfiles import StaticFiles

app = FastAPI()

data_buku = [
    {
        "id": 1,
        "judul": "Laskar Pelangi",
        "penulis": "Andrea hirata",
        "tahun": 2005,
        "genre": "novel",
        "tersedia": True
    },
    {
        "id": 2,
        "judul": "Bumi",
        "penulis": "Tere Liye",
        "tahun": 2014,
        "genre": "fantasty",
        "tersedia": False
    }
]

class BukuBase(BaseModel):
    id: int
    judul: str
    penulis: str
    tahun: int
    genre: str
    tersedia: bool

class Buku(BaseModel):
    judul: str
    penulis: str
    tahun: int
    genre: str
    tersedia: bool
    
class ResultBuku(BaseModel):
    status: int
    pesan: str
    data: BukuBase
    
@app.get("/buku")
async def get_buku(id: Annotated[int | None, Query()] = None, judul: Annotated[str | None, Query()] = None):
    
    if id is not None or judul is not None:
        result_data_buku = next((item_buku for item_buku in data_buku if (id is not None and item_buku["id"] == id) or (judul is not None and item_buku["judul"].lower() == judul.lower())), None)
        
        # if id not in data_buku:
        if result_data_buku is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"buku tidak ditemukan",
            )
        
        return {
            "status": status.HTTP_200_OK, 
            "pesan": f"List data buku berhasil terload (total len(result_data_buku) buku)",
            "data": result_data_buku
        }
    
    
    return {
        "status": status.HTTP_200_OK, 
        "pesan": f"List data buku berhasil terload (total len(result_data_buku) buku)",
        "data": data_buku
    }

@app.get("/buku/{id}")
async def get_buku_id(id: int) -> ResultBuku:
    
    result_data_buku = next((item_buku for item_buku in data_buku if item_buku["id"] == id),None)

    if result_data_buku is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"buku id {id} tidak ditemukan")

    return {
        "status": status.HTTP_200_OK, 
        "pesan": f"Data buku id {id} ditemukan",
        "data": result_data_buku
    }

@app.post("/buku", status_code=status.HTTP_201_CREATED, response_model=ResultBuku)
async def add_buku(buku: Buku):
    
    if not data_buku:
        id_buku = 1
    
    else:
        
        list_id_buku = [item_buku.get("id") for item_buku in data_buku]
        
        # id_buku = len(data_buku) + 1
        id_buku = max(list_id_buku) + 1
    
    result_data_buku = jsonable_encoder(buku)
    result_data_buku["id"] = id_buku
    data_buku.append(result_data_buku)
    
    return {
        "status": status.HTTP_201_CREATED, 
        "pesan": f"Data buku baru berhasil ditambahkan ke list",
        "data": result_data_buku
    }

@app.put("/buku/{id}", response_model=ResultBuku)
async def update_buku(id: int, buku: Buku):
    
    index_buku = next((index for index, item_buku in enumerate(data_buku) if item_buku["id"] == id),None)
    
    if index_buku is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Buku id {id} tidak ditemukan"
        )
        
    else:
        result_update_buku = jsonable_encoder(buku)
        result_update_buku["id"] = id
        data_buku[index_buku] = result_update_buku
        
        return {
            "status": status.HTTP_201_CREATED, 
            "pesan": f"Data buku id {id} berhasil diupdate",
            "data": result_update_buku
        }

@app.delete("/buku/{id}")
async def delete_buku(id: int):
    index_buku = next((index for index, item_buku in enumerate(data_buku) if item_buku["id"] == id), None)
    
    if index_buku is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Data buku id {id} tidak ditemukan")
    
    del data_buku[index_buku]
    
    return JSONResponse(
        content=f"Data Buku Id {id} berhasil dihapus",
        status_code=status.HTTP_200_OK
        
    )
    
@app.patch("/buku/{id}")
async def update_status_buku(id: int, tersedia: bool):
    index_buku = next((index for index, item_buku in enumerate(data_buku) if item_buku["id"] == id), None)
    
    if index_buku is not None:
        data_buku[index_buku]["tersedia"] = tersedia
        
        return data_buku[index_buku]
        
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=f"Data buku id {id} tidak ditemukan"
    )
    
    
origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8080",
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
