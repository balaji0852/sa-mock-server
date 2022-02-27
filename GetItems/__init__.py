import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    return func.HttpResponse(json.dumps({
   "items":[
      {
         "itemID":1,
         "productID":"6ecd5726-a6af-4b6e-9334-df0101ea202a",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6ecd5726-a6af-4b6e-9334-df0101ea202a.jpg",
         "itemDetails":"peter england beige pant",
         "category":"pant",
         "price":599,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":2,
         "productID":"8b8563c5-9eb1-4c44-9d52-acd22a8fe25d",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/8b8563c5-9eb1-4c44-9d52-acd22a8fe25d.jpg",
         "itemDetails":"uspn beige pant",
         "category":"pant",
         "price":759,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":3,
         "productID":"8c6763e1-9239-438a-84cb-f4a896d2f46f",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/8c6763e1-9239-438a-84cb-f4a896d2f46f.jpg",
         "itemDetails":"crocodile beige pant",
         "category":"pant",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":4,
         "productID":"37a0cfa8-0f10-405a-8d48-838a3d687620",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/37a0cfa8-0f10-405a-8d48-838a3d687620.jpg",
         "itemDetails":"peter england beige pant",
         "category":"pant",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":5,
         "productID":"42cf9e7a-1ad2-4b91-9691-a65511341c05",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/42cf9e7a-1ad2-4b91-9691-a65511341c05.jpg",
         "itemDetails":"roadster beige pant",
         "category":"pant",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":6,
         "productID":"59da8ee6-32a7-44f0-abf2-b53b1f6448af",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/59da8ee6-32a7-44f0-abf2-b53b1f6448af.jpg",
         "itemDetails":"levis beige pant",
         "category":"pant",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":7,
         "productID":"297b1d2d-70d6-42d9-a6eb-5d28c59f1061",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/297b1d2d-70d6-42d9-a6eb-5d28c59f1061.jpg",
         "itemDetails":"peter england beige pant",
         "category":"pant",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":8,
         "productID":"510f1ddc-4984-4c98-8485-a22193eda539",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/510f1ddc-4984-4c98-8485-a22193eda539.jpg",
         "itemDetails":"roadster beige pant",
         "category":"pant",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"beige"
      },
      {
         "itemID":9,
         "productID":"0c2eb9ff-7f26-492d-9957-0d845669685f",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0c2eb9ff-7f26-492d-9957-0d845669685f.jpg",
         "itemDetails":"crocodile black pant",
         "category":"pant",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":10,
         "productID":"0c224954-0e0f-4caa-82c8-cf9581e89336",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0c224954-0e0f-4caa-82c8-cf9581e89336.jpg",
         "itemDetails":"uspn black pant",
         "category":"pant",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":11,
         "productID":"1a08f33a-2ff4-4fb8-920b-8ff514bcdda8",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1a08f33a-2ff4-4fb8-920b-8ff514bcdda8.jpg",
         "itemDetails":"levis black pant",
         "category":"pant",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":12,
         "productID":"1bb71a5d-a665-4d72-9e06-b7892a8a7e92",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1bb71a5d-a665-4d72-9e06-b7892a8a7e92.jpg",
         "itemDetails":"peter england black pant",
         "category":"pant",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":13,
         "productID":"2a1f8d1f-301c-4a6d-87e1-fab1660a6a82",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2a1f8d1f-301c-4a6d-87e1-fab1660a6a82.jpg",
         "itemDetails":"peter england black pant",
         "category":"pant",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":14,
         "productID":"74e2adaf-72e7-405c-8e79-7dd804353143",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/74e2adaf-72e7-405c-8e79-7dd804353143.jpg",
         "itemDetails":"uspn black pant",
         "category":"pant",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":15,
         "productID":"1b065c3c-0679-40af-9924-8de9986fdf66",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1b065c3c-0679-40af-9924-8de9986fdf66.jpg",
         "itemDetails":"peter england blue pant",
         "category":"pant",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":16,
         "productID":"1ca03195-b1e8-4c47-85de-81a942ea561e",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1ca03195-b1e8-4c47-85de-81a942ea561e.jpg",
         "itemDetails":"levis blue pant",
         "category":"pant",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":17,
         "productID":"1d42c614-19d5-4515-8ef9-0bf551a601c0",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1d42c614-19d5-4515-8ef9-0bf551a601c0.jpg",
         "itemDetails":"uspn blue pant",
         "category":"pant",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":18,
         "productID":"1ed97cea-53f2-4342-8ac2-9083c936eef6",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1ed97cea-53f2-4342-8ac2-9083c936eef6.jpg",
         "itemDetails":"crocodile blue pant",
         "category":"pant",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":19,
         "productID":"1faab1ac-d8d4-4711-adbb-7812d7513d41",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1faab1ac-d8d4-4711-adbb-7812d7513d41.jpg",
         "itemDetails":"levis blue pant",
         "category":"pant",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":20,
         "productID":"02f749c2-1c47-4f4a-bd83-4df75df91e1f",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/02f749c2-1c47-4f4a-bd83-4df75df91e1f.jpg",
         "itemDetails":"uspn blue pant",
         "category":"pant",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":21,
         "productID":"2adfd297-5e23-449b-bb28-b35a361b4645",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2adfd297-5e23-449b-bb28-b35a361b4645.jpg",
         "itemDetails":"levis blue pant",
         "category":"pant",
         "price":599,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":22,
         "productID":"2dc14f11-7be1-4f03-a1c9-f8407f92d958",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2dc14f11-7be1-4f03-a1c9-f8407f92d958.jpg",
         "itemDetails":"crocodile blue pant",
         "category":"pant",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":23,
         "productID":"2f0b7b04-c238-465b-8e7a-08fabec28223",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2f0b7b04-c238-465b-8e7a-08fabec28223.jpg",
         "itemDetails":"uspn blue pant",
         "category":"pant",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":24,
         "productID":"4ba6deca-32d4-414a-8ccc-42bee703520d",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4ba6deca-32d4-414a-8ccc-42bee703520d.jpg",
         "itemDetails":"peter england blue pant",
         "category":"pant",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":25,
         "productID":"4c9dc9d8-07a9-40c8-89b0-33c9e51e87ef",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4c9dc9d8-07a9-40c8-89b0-33c9e51e87ef.jpg",
         "itemDetails":"peter england blue pant",
         "category":"pant",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":26,
         "productID":"4cc4e673-fecd-4e4e-a7eb-f2efd39a5291",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4cc4e673-fecd-4e4e-a7eb-f2efd39a5291.jpg",
         "itemDetails":"levis blue pant",
         "category":"pant",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":27,
         "productID":"4cdf0860-1969-43db-9d4e-b255158c8fa0",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4cdf0860-1969-43db-9d4e-b255158c8fa0.jpg",
         "itemDetails":"roadster blue pant",
         "category":"pant",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":28,
         "productID":"5d6be0e5-7d7c-4105-b00c-251d62737863",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5d6be0e5-7d7c-4105-b00c-251d62737863.jpg",
         "itemDetails":"uspn blue pant",
         "category":"pant",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":29,
         "productID":"5fcc9116-4153-4438-8024-f0ea54c3b40f",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5fcc9116-4153-4438-8024-f0ea54c3b40f.jpg",
         "itemDetails":"crocodile blue pant",
         "category":"pant",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":30,
         "productID":"0a7e5fe0-d592-40e6-b9b8-75aac9a2d685",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0a7e5fe0-d592-40e6-b9b8-75aac9a2d685.jpg",
         "itemDetails":"uspn red pant",
         "category":"pant",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":31,
         "productID":"1ed97cea-53f2-4342-8ac2-9083c936eef6",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1ed97cea-53f2-4342-8ac2-9083c936eef6.jpg",
         "itemDetails":"peter england red pant",
         "category":"pant",
         "price":759,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":32,
         "productID":"2ddda978-3941-444b-87ac-8ff4f2806da6",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2ddda978-3941-444b-87ac-8ff4f2806da6.jpg",
         "itemDetails":"crocodile red pant",
         "category":"pant",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":33,
         "productID":"03a43dea-405e-4a11-9716-2f790a95f699",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/03a43dea-405e-4a11-9716-2f790a95f699.jpg",
         "itemDetails":"levis red pant",
         "category":"pant",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":34,
         "productID":"4e087288-681e-4722-b9e5-929033c5d23e",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4e087288-681e-4722-b9e5-929033c5d23e.jpg",
         "itemDetails":"roadster red pant",
         "category":"pant",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":35,
         "productID":"6c5ce8a8-6960-4b64-b357-36a9399ce146",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6c5ce8a8-6960-4b64-b357-36a9399ce146.jpg",
         "itemDetails":"levis red pant",
         "category":"pant",
         "price":599,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":36,
         "productID":"6c86fcb8-3bb1-4b70-bf96-b756b992a9f9",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6c86fcb8-3bb1-4b70-bf96-b756b992a9f9.jpg",
         "itemDetails":"uspn red pant",
         "category":"pant",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":37,
         "productID":"7eed8816-32bc-441b-8f7a-aa6ac2557ce5",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/7eed8816-32bc-441b-8f7a-aa6ac2557ce5.jpg",
         "itemDetails":"peter england red pant",
         "category":"pant",
         "price":759,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":38,
         "productID":"45d99d85-955a-4fc3-bbb8-4429e40a3233",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/45d99d85-955a-4fc3-bbb8-4429e40a3233.jpg",
         "itemDetails":"peter england red pant",
         "category":"pant",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":39,
         "productID":"95df0f8a-5c06-4ee0-877f-b4f4858c55bf",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/95df0f8a-5c06-4ee0-877f-b4f4858c55bf.jpg",
         "itemDetails":"peter england red pant",
         "category":"pant",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":40,
         "productID":"137ef939-62db-460f-9102-120dc1ffeeec",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/137ef939-62db-460f-9102-120dc1ffeeec.jpg",
         "itemDetails":"crocodile red pant",
         "category":"pant",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":41,
         "productID":"303d4ddf-0d8a-4389-9943-b5fd0fc0843f",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/303d4ddf-0d8a-4389-9943-b5fd0fc0843f.jpg",
         "itemDetails":"roadster red pant",
         "category":"pant",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":42,
         "productID":"0ad5bfb5-0f2b-4396-8c05-39ca0a9a2960",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0ad5bfb5-0f2b-4396-8c05-39ca0a9a2960.jpg",
         "itemDetails":"crocodile white pant",
         "category":"pant",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":43,
         "productID":"0c99f0b4-3a0d-4d24-bfdd-e9e98914892c",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0c99f0b4-3a0d-4d24-bfdd-e9e98914892c.jpg",
         "itemDetails":"levis white pant",
         "category":"pant",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":44,
         "productID":"4f240f86-4530-44ad-aae1-4e2d781ad6be",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4f240f86-4530-44ad-aae1-4e2d781ad6be.jpg",
         "itemDetails":"crocodile white pant",
         "category":"pant",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":45,
         "productID":"6b2a4812-5f04-40ca-aba3-f66607934a7e",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6b2a4812-5f04-40ca-aba3-f66607934a7e.jpg",
         "itemDetails":"peter england white pant",
         "category":"pant",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":46,
         "productID":"9a87b9e5-ac39-4b3a-b550-ac2d5c38b2d6",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/9a87b9e5-ac39-4b3a-b550-ac2d5c38b2d6.jpg",
         "itemDetails":"roadster white pant",
         "category":"pant",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":47,
         "productID":"40ee6784-5c49-40c1-bf26-7cdbcc9ff849",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/40ee6784-5c49-40c1-bf26-7cdbcc9ff849.jpg",
         "itemDetails":"roadster white pant",
         "category":"pant",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":48,
         "productID":"49eb3fa7-099d-45e8-88b0-35b60b42e386",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/49eb3fa7-099d-45e8-88b0-35b60b42e386.jpg",
         "itemDetails":"levis white pant",
         "category":"pant",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":49,
         "productID":"201d7c0c-4e6f-47c9-bb55-44890164c6a7",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/201d7c0c-4e6f-47c9-bb55-44890164c6a7.jpg",
         "itemDetails":"peter england white pant",
         "category":"pant",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":50,
         "productID":"4be01935-1fff-4595-aac4-b0a0963b4706",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4be01935-1fff-4595-aac4-b0a0963b4706.jpg",
         "itemDetails":"levis black shoe",
         "category":"shoe",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":51,
         "productID":"4c471b57-0825-4544-8bc3-6ec241c2baca",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4c471b57-0825-4544-8bc3-6ec241c2baca.jpg",
         "itemDetails":"crocodile black shoe",
         "category":"shoe",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":52,
         "productID":"4eba049d-e813-4af9-913a-53b6877cdda2",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4eba049d-e813-4af9-913a-53b6877cdda2.jpg",
         "itemDetails":"crocodile black shoe",
         "category":"shoe",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":53,
         "productID":"5fd435b0-c255-4200-ada3-09658ce35bb5",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5fd435b0-c255-4200-ada3-09658ce35bb5.jpg",
         "itemDetails":"peter england black shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":54,
         "productID":"8c2759e4-2ff5-4cf8-8ac9-88501c634cae",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/8c2759e4-2ff5-4cf8-8ac9-88501c634cae.jpg",
         "itemDetails":"roadster black shoe",
         "category":"shoe",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":55,
         "productID":"8e34ebaa-6919-46f3-84e0-98800a00f524",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/8e34ebaa-6919-46f3-84e0-98800a00f524.jpg",
         "itemDetails":"crocodile black shoe",
         "category":"shoe",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":56,
         "productID":"8f945c82-4d26-4c26-a525-bd785b7d73c9",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/8f945c82-4d26-4c26-a525-bd785b7d73c9.jpg",
         "itemDetails":"uspn black shoe",
         "category":"shoe",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":57,
         "productID":"9a7ca413-4c0a-4800-8f08-95e491336b4d",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/9a7ca413-4c0a-4800-8f08-95e491336b4d.jpg",
         "itemDetails":"crocodile black shoe",
         "category":"shoe",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":58,
         "productID":"17f835b2-a006-42a3-8ce8-d16b593a8d11",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/17f835b2-a006-42a3-8ce8-d16b593a8d11.jpg",
         "itemDetails":"roadster black shoe",
         "category":"shoe",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":59,
         "productID":"f804b775-13a3-4913-8006-5a1e61f7a005",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/f804b775-13a3-4913-8006-5a1e61f7a005.jpg",
         "itemDetails":"crocodile black shoe",
         "category":"shoe",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":60,
         "productID":"fcd313d2-0e91-450d-a613-e9f5e91a47da",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/fcd313d2-0e91-450d-a613-e9f5e91a47da.jpg",
         "itemDetails":"levis black shoe",
         "category":"shoe",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":61,
         "productID":"2be8cf7a-5b2e-400f-a826-785997af532a",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2be8cf7a-5b2e-400f-a826-785997af532a.jpg",
         "itemDetails":"roadster blue shoe",
         "category":"shoe",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":62,
         "productID":"7bb0226b-f068-4b46-9e40-1e5110319fcd",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/7bb0226b-f068-4b46-9e40-1e5110319fcd.jpg",
         "itemDetails":"uspn blue shoe",
         "category":"shoe",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":63,
         "productID":"9b68ea5b-6589-4468-bad4-231cf47a60ae",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/9b68ea5b-6589-4468-bad4-231cf47a60ae.jpg",
         "itemDetails":"crocodile blue shoe",
         "category":"shoe",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":64,
         "productID":"a0207dce-3e5b-4ac1-92b9-59c6a31c516f",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/a0207dce-3e5b-4ac1-92b9-59c6a31c516f.jpg",
         "itemDetails":"uspn blue shoe",
         "category":"shoe",
         "price":759,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":65,
         "productID":"b5b1359c-f143-4955-a523-25c240777b9b",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b5b1359c-f143-4955-a523-25c240777b9b.jpg",
         "itemDetails":"peter england blue shoe",
         "category":"shoe",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":66,
         "productID":"b554f97c-8eaf-405a-8cbc-b80304c2da94",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b554f97c-8eaf-405a-8cbc-b80304c2da94.jpg",
         "itemDetails":"peter england blue shoe",
         "category":"shoe",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":67,
         "productID":"ca045c6f-5bb5-4e8f-ae75-b177c01e6137",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/ca045c6f-5bb5-4e8f-ae75-b177c01e6137.jpg",
         "itemDetails":"crocodile blue shoe",
         "category":"shoe",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":68,
         "productID":"da73c56d-32ac-4d66-bdb2-82c50adcdde7",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/da73c56d-32ac-4d66-bdb2-82c50adcdde7.jpg",
         "itemDetails":"levis blue shoe",
         "category":"shoe",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":69,
         "productID":"3a5f03b9-9afb-4fd4-bc3e-2eb56f83801d",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/3a5f03b9-9afb-4fd4-bc3e-2eb56f83801d.jpg",
         "itemDetails":"roadster brown shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":70,
         "productID":"5e577f40-dd22-4b40-9827-ce6cae5ac3fd",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5e577f40-dd22-4b40-9827-ce6cae5ac3fd.jpg",
         "itemDetails":"roadster brown shoe",
         "category":"shoe",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":71,
         "productID":"5fea042c-f2ac-4523-a813-fc0eae2d9472",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5fea042c-f2ac-4523-a813-fc0eae2d9472.jpg",
         "itemDetails":"levis brown shoe",
         "category":"shoe",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":72,
         "productID":"6bdd35ce-9285-4580-8755-4c8f4bd9b724",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6bdd35ce-9285-4580-8755-4c8f4bd9b724.jpg",
         "itemDetails":"roadster brown shoe",
         "category":"shoe",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":73,
         "productID":"6f16e53a-4a25-4c8e-9dbf-705c682b1f87",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6f16e53a-4a25-4c8e-9dbf-705c682b1f87.jpg",
         "itemDetails":"crocodile brown shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":74,
         "productID":"7d5a20ff-6431-404e-9870-78140166cf7a",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/7d5a20ff-6431-404e-9870-78140166cf7a.jpg",
         "itemDetails":"crocodile brown shoe",
         "category":"shoe",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":75,
         "productID":"7e020806-9182-44e5-a9a2-89a88f06f047",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/7e020806-9182-44e5-a9a2-89a88f06f047.jpg",
         "itemDetails":"roadster brown shoe",
         "category":"shoe",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":76,
         "productID":"8dc068c8-245a-4d42-9beb-d704fb7d3feb",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/8dc068c8-245a-4d42-9beb-d704fb7d3feb.jpg",
         "itemDetails":"roadster brown shoe",
         "category":"shoe",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":77,
         "productID":"9ae53cee-51b6-4255-88b9-836b9c8903f4",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/9ae53cee-51b6-4255-88b9-836b9c8903f4.jpg",
         "itemDetails":"peter england brown shoe",
         "category":"shoe",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":78,
         "productID":"98e89103-64e3-41db-adc0-f83726f757d5",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/98e89103-64e3-41db-adc0-f83726f757d5.jpg",
         "itemDetails":"uspn brown shoe",
         "category":"shoe",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":79,
         "productID":"132e5fa5-ed38-4293-8dff-20727b6b5ac2",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/132e5fa5-ed38-4293-8dff-20727b6b5ac2.jpg",
         "itemDetails":"roadster brown shoe",
         "category":"shoe",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":80,
         "productID":"9488678d-38f9-4888-b117-28a982ecf6f5",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/9488678d-38f9-4888-b117-28a982ecf6f5.jpg",
         "itemDetails":"uspn brown shoe",
         "category":"shoe",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":81,
         "productID":"d0ccaaad-7e82-4834-ad38-5dc4440d7e6e",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/d0ccaaad-7e82-4834-ad38-5dc4440d7e6e.jpg",
         "itemDetails":"levis brown shoe",
         "category":"shoe",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"brown"
      },
      {
         "itemID":82,
         "productID":"18ff3e0e-6676-4f26-8be4-a992217ac524",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/18ff3e0e-6676-4f26-8be4-a992217ac524.jpg",
         "itemDetails":"peter england green shoe",
         "category":"shoe",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"green"
      },
      {
         "itemID":83,
         "productID":"3cf61c2b-7afa-4e63-8cbf-c163290dc67b",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/3cf61c2b-7afa-4e63-8cbf-c163290dc67b.jpg",
         "itemDetails":"crocodile pink shoe",
         "category":"shoe",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":84,
         "productID":"6d36bed9-c236-4bc0-81af-99bc657419bc",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6d36bed9-c236-4bc0-81af-99bc657419bc.jpg",
         "itemDetails":"uspn pink shoe",
         "category":"shoe",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":85,
         "productID":"7d0a2ea3-e1ef-40d7-9d37-542778df3340",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/7d0a2ea3-e1ef-40d7-9d37-542778df3340.jpg",
         "itemDetails":"roadster pink shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":86,
         "productID":"261b36f3-5c90-4d89-93d2-0d20a7782287",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/261b36f3-5c90-4d89-93d2-0d20a7782287.jpg",
         "itemDetails":"crocodile pink shoe",
         "category":"shoe",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":87,
         "productID":"1558e0ca-2ef3-402e-bf6c-d2d62c974cd4",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1558e0ca-2ef3-402e-bf6c-d2d62c974cd4.jpg",
         "itemDetails":"crocodile pink shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":88,
         "productID":"a7b367e2-59ef-48c2-93d7-bd3d17a12c3a",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/a7b367e2-59ef-48c2-93d7-bd3d17a12c3a.jpg",
         "itemDetails":"peter england pink shoe",
         "category":"shoe",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":89,
         "productID":"ac8a9f3c-6436-4bfa-8a08-978ec833045c",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/ac8a9f3c-6436-4bfa-8a08-978ec833045c.jpg",
         "itemDetails":"peter england pink shoe",
         "category":"shoe",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":90,
         "productID":"b3586849-9c97-4f0b-81cf-80664fe91e08",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b3586849-9c97-4f0b-81cf-80664fe91e08.jpg",
         "itemDetails":"levis pink shoe",
         "category":"shoe",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":91,
         "productID":"d4e28f4e-4575-4183-86fd-4c71105bd426",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/d4e28f4e-4575-4183-86fd-4c71105bd426.jpg",
         "itemDetails":"crocodile pink shoe",
         "category":"shoe",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":92,
         "productID":"fb9e862c-8c64-4f23-b1e9-e734ec797436",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/fb9e862c-8c64-4f23-b1e9-e734ec797436.jpg",
         "itemDetails":"levis pink shoe",
         "category":"shoe",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":93,
         "productID":"ff5b1764-1272-41bf-a324-98f1b9f13fae",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/ff5b1764-1272-41bf-a324-98f1b9f13fae.jpg",
         "itemDetails":"peter england pink shoe",
         "category":"shoe",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"pink"
      },
      {
         "itemID":94,
         "productID":"9c97e52f-7cf4-4aa5-87e4-c3478108aa22",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/9c97e52f-7cf4-4aa5-87e4-c3478108aa22.jpg",
         "itemDetails":"roadster red shoe",
         "category":"shoe",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":95,
         "productID":"84cfca64-c7c9-427b-af29-6afa22ce7a8d",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/84cfca64-c7c9-427b-af29-6afa22ce7a8d.jpg",
         "itemDetails":"levis red shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":96,
         "productID":"765235f1-0e47-436f-8d09-665463c8c6ca",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/765235f1-0e47-436f-8d09-665463c8c6ca.jpg",
         "itemDetails":"roadster red shoe",
         "category":"shoe",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":97,
         "productID":"ab70eea8-6103-4dbc-a135-8085d222f03a",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/ab70eea8-6103-4dbc-a135-8085d222f03a.jpg",
         "itemDetails":"crocodile red shoe",
         "category":"shoe",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":98,
         "productID":"d4347691-a801-44a8-8e6d-87faea3db2a3",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/d4347691-a801-44a8-8e6d-87faea3db2a3.jpg",
         "itemDetails":"levis red shoe",
         "category":"shoe",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":99,
         "productID":"f5ed50b6-79b3-4d9d-84a9-8010f5e1c581",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/f5ed50b6-79b3-4d9d-84a9-8010f5e1c581.jpg",
         "itemDetails":"peter england red shoe",
         "category":"shoe",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":100,
         "productID":"1e170a9f-9437-4eae-bd67-389c48b93ff9",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1e170a9f-9437-4eae-bd67-389c48b93ff9.jpg",
         "itemDetails":"roadster white shoe",
         "category":"shoe",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":101,
         "productID":"2b54e651-5d43-4f24-9e9e-a58ce16d7c88",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2b54e651-5d43-4f24-9e9e-a58ce16d7c88.jpg",
         "itemDetails":"levis white shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":102,
         "productID":"5f838a1c-6ab5-4629-a7cb-4a4755d408bb",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5f838a1c-6ab5-4629-a7cb-4a4755d408bb.jpg",
         "itemDetails":"levis white shoe",
         "category":"shoe",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":103,
         "productID":"562fcdc1-cda7-40cd-bb7b-9b2c908d0931",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/562fcdc1-cda7-40cd-bb7b-9b2c908d0931.jpg",
         "itemDetails":"uspn white shoe",
         "category":"shoe",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":104,
         "productID":"669d3343-bda1-4a33-8f5c-3f20e2807a1f",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/669d3343-bda1-4a33-8f5c-3f20e2807a1f.jpg",
         "itemDetails":"roadster white shoe",
         "category":"shoe",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":105,
         "productID":"604486df-573b-4eb7-9c78-7b0a5b1b7392",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/604486df-573b-4eb7-9c78-7b0a5b1b7392.jpg",
         "itemDetails":"peter england white shoe",
         "category":"shoe",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":106,
         "productID":"b6c29a96-b6f5-4b91-ab45-e6727d02ad2d",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b6c29a96-b6f5-4b91-ab45-e6727d02ad2d.jpg",
         "itemDetails":"crocodile white shoe",
         "category":"shoe",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":107,
         "productID":"b232d13e-54fc-4c3a-9479-040932738ab3",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b232d13e-54fc-4c3a-9479-040932738ab3.jpg",
         "itemDetails":"uspn white shoe",
         "category":"shoe",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":108,
         "productID":"bbd52702-8038-4658-bcab-d6ee6586dd01",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/bbd52702-8038-4658-bcab-d6ee6586dd01.jpg",
         "itemDetails":"peter england white shoe",
         "category":"shoe",
         "price":249,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":109,
         "productID":"c79342a6-6642-43f2-9822-a4eb22ebceb6",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/c79342a6-6642-43f2-9822-a4eb22ebceb6.jpg",
         "itemDetails":"uspn white shoe",
         "category":"shoe",
         "price":759,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":110,
         "productID":"0dd87e47-ca85-4d5c-9fd1-59f5a01eb656",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0dd87e47-ca85-4d5c-9fd1-59f5a01eb656.jpg",
         "itemDetails":"roadster yellow shoe",
         "category":"shoe",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"yellow"
      },
      {
         "itemID":111,
         "productID":"e2dd7cf5-e947-4f6f-b8c1-5014322954b7",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/e2dd7cf5-e947-4f6f-b8c1-5014322954b7.jpg",
         "itemDetails":"peter england yellow shoe",
         "category":"shoe",
         "price":599,
         "locationName":"bangalore",
         "sub_category":"yellow"
      },
      {
         "itemID":112,
         "productID":"3d20c462-34a4-4501-9c91-f6d3a9684715",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/3d20c462-34a4-4501-9c91-f6d3a9684715.jpg",
         "itemDetails":"peter england black shirt",
         "category":"shirt",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":113,
         "productID":"7aefbf16-da20-4836-b31f-ec61d161b4b9",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/7aefbf16-da20-4836-b31f-ec61d161b4b9.jpg",
         "itemDetails":"crocodile black shirt",
         "category":"shirt",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":114,
         "productID":"380f132c-02c5-4724-9daa-9633e9957940",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/380f132c-02c5-4724-9daa-9633e9957940.jpg",
         "itemDetails":"roadster black shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":115,
         "productID":"38186e67-f333-4fd1-9817-039ff3d2170c",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/38186e67-f333-4fd1-9817-039ff3d2170c.jpg",
         "itemDetails":"roadster black shirt",
         "category":"shirt",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":116,
         "productID":"556761df-ffc1-4af4-aaf9-80425f50fb8b",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/556761df-ffc1-4af4-aaf9-80425f50fb8b.jpg",
         "itemDetails":"levis black shirt",
         "category":"shirt",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"black"
      },
      {
         "itemID":117,
         "productID":"1b00c860-4121-475e-8991-a26247be3145",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1b00c860-4121-475e-8991-a26247be3145.jpg",
         "itemDetails":"peter england blue shirt",
         "category":"shirt",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":118,
         "productID":"1fd8e843-be30-4d20-a386-909b3f89c075",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1fd8e843-be30-4d20-a386-909b3f89c075.jpg",
         "itemDetails":"uspn blue shirt",
         "category":"shirt",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":119,
         "productID":"3bc940a9-c72f-4afb-ae60-6f65e01a507d",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/3bc940a9-c72f-4afb-ae60-6f65e01a507d.jpg",
         "itemDetails":"uspn blue shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":120,
         "productID":"4ecf5b79-2a31-4006-aa36-76f62b6fa24c",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4ecf5b79-2a31-4006-aa36-76f62b6fa24c.jpg",
         "itemDetails":"uspn blue shirt",
         "category":"shirt",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":121,
         "productID":"4ed9377d-7682-4882-a0f3-af7d43da1e9b",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4ed9377d-7682-4882-a0f3-af7d43da1e9b.jpg",
         "itemDetails":"peter england blue shirt",
         "category":"shirt",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":122,
         "productID":"005d3a4d-b8cc-4f14-a288-8065ab797974",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/005d3a4d-b8cc-4f14-a288-8065ab797974.jpg",
         "itemDetails":"crocodile blue shirt",
         "category":"shirt",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":123,
         "productID":"6e9dadfd-1617-4216-909b-e77d4dd89ec3",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6e9dadfd-1617-4216-909b-e77d4dd89ec3.jpg",
         "itemDetails":"levis blue shirt",
         "category":"shirt",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":124,
         "productID":"8de3baf1-0422-4f6c-beca-6ace1f0b8730",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/8de3baf1-0422-4f6c-beca-6ace1f0b8730.jpg",
         "itemDetails":"peter england blue shirt",
         "category":"shirt",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":125,
         "productID":"69504219-eb76-41d3-8ef3-9b3e1030d649",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/69504219-eb76-41d3-8ef3-9b3e1030d649.jpg",
         "itemDetails":"peter england blue shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":126,
         "productID":"b6bc8c5d-26df-4750-8c80-c092f3e1e514",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b6bc8c5d-26df-4750-8c80-c092f3e1e514.jpg",
         "itemDetails":"crocodile blue shirt",
         "category":"shirt",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"blue"
      },
      {
         "itemID":127,
         "productID":"76f75142-fc3f-49da-96c3-4e115c81183b",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/76f75142-fc3f-49da-96c3-4e115c81183b.jpg",
         "itemDetails":"peter england green shirt",
         "category":"shirt",
         "price":899,
         "locationName":"bangalore",
         "sub_category":"green"
      },
      {
         "itemID":128,
         "productID":"420a80c4-dfc9-4cc3-8de6-42765b92bb4b",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/420a80c4-dfc9-4cc3-8de6-42765b92bb4b.jpg",
         "itemDetails":"roadster green shirt",
         "category":"shirt",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"green"
      },
      {
         "itemID":129,
         "productID":"751b991d-99ce-4a5e-b76c-090ef19e638c",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/751b991d-99ce-4a5e-b76c-090ef19e638c.jpg",
         "itemDetails":"peter england green shirt",
         "category":"shirt",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"green"
      },
      {
         "itemID":130,
         "productID":"4245ab7f-8b51-407d-a63b-a3c7fc5007c4",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4245ab7f-8b51-407d-a63b-a3c7fc5007c4.jpg",
         "itemDetails":"levis green shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"green"
      },
      {
         "itemID":131,
         "productID":"12162c30-f6c8-4054-9f35-937629373cca",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/12162c30-f6c8-4054-9f35-937629373cca.jpg",
         "itemDetails":"uspn green shirt",
         "category":"shirt",
         "price":599,
         "locationName":"bangalore",
         "sub_category":"green"
      },
      {
         "itemID":132,
         "productID":"31547719-bfd1-404d-bc3f-d341489be26d",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/31547719-bfd1-404d-bc3f-d341489be26d.jpg",
         "itemDetails":"crocodile grey shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"grey"
      },
      {
         "itemID":133,
         "productID":"a848af08-9844-41f3-b582-2897afc331d3",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/a848af08-9844-41f3-b582-2897afc331d3.jpg",
         "itemDetails":"peter england grey shirt",
         "category":"shirt",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"grey"
      },
      {
         "itemID":134,
         "productID":"00e745c9-97d9-429d-8c3f-d3db7a2d2991",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/00e745c9-97d9-429d-8c3f-d3db7a2d2991.jpg",
         "itemDetails":"levis red shirt",
         "category":"shirt",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":135,
         "productID":"9f41bab0-b7f6-41e3-8482-e0632735eebf",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/9f41bab0-b7f6-41e3-8482-e0632735eebf.jpg",
         "itemDetails":"uspn red shirt",
         "category":"shirt",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":136,
         "productID":"99a130ca-5fe5-4f68-afd6-830e26baf2c8",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/99a130ca-5fe5-4f68-afd6-830e26baf2c8.jpg",
         "itemDetails":"peter england red shirt",
         "category":"shirt",
         "price":799,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":137,
         "productID":"6360b20c-f47e-4ed0-b195-fa118461a49f",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6360b20c-f47e-4ed0-b195-fa118461a49f.jpg",
         "itemDetails":"crocodile red shirt",
         "category":"shirt",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":138,
         "productID":"6698ff1d-1214-467d-a0e9-2d65ab4fba0b",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6698ff1d-1214-467d-a0e9-2d65ab4fba0b.jpg",
         "itemDetails":"levis red shirt",
         "category":"shirt",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":139,
         "productID":"56606e8d-8092-4541-9ac7-92ada184d3c1",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/56606e8d-8092-4541-9ac7-92ada184d3c1.jpg",
         "itemDetails":"levis red shirt",
         "category":"shirt",
         "price":759,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":140,
         "productID":"94287d7c-aa4c-4dc3-b728-0a239badefb7",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/94287d7c-aa4c-4dc3-b728-0a239badefb7.jpg",
         "itemDetails":"uspn red shirt",
         "category":"shirt",
         "price":549,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":141,
         "productID":"2577536d-e1cd-47c5-a701-4c4d910384d1",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2577536d-e1cd-47c5-a701-4c4d910384d1.jpg",
         "itemDetails":"levis red shirt",
         "category":"shirt",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":142,
         "productID":"a6153f06-bb9a-4303-b36c-80ffb61a9565",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/a6153f06-bb9a-4303-b36c-80ffb61a9565.jpg",
         "itemDetails":"roadster red shirt",
         "category":"shirt",
         "price":349,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":143,
         "productID":"adf010f4-3f9c-434f-93bb-cbfd6dddf931",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/adf010f4-3f9c-434f-93bb-cbfd6dddf931.jpg",
         "itemDetails":"peter england red shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":144,
         "productID":"b0c03127-9dfb-4573-8934-1958396937bf",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b0c03127-9dfb-4573-8934-1958396937bf.jpg",
         "itemDetails":"levis red shirt",
         "category":"shirt",
         "price":499,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":145,
         "productID":"b4b507dd-f68c-4fd1-9f25-6e2c2930a569",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/b4b507dd-f68c-4fd1-9f25-6e2c2930a569.jpg",
         "itemDetails":"uspn red shirt",
         "category":"shirt",
         "price":901,
         "locationName":"bangalore",
         "sub_category":"red"
      },
      {
         "itemID":146,
         "productID":"0a77dbed-06fb-4ba7-b1e3-24f3a41498bc",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0a77dbed-06fb-4ba7-b1e3-24f3a41498bc.jpg",
         "itemDetails":"uspn white shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":147,
         "productID":"0a77dbed-06fb-4ba7-b1e3-24f3a41498bc",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/0a77dbed-06fb-4ba7-b1e3-24f3a41498bc.jpg",
         "itemDetails":"crocodile white shirt",
         "category":"shirt",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":148,
         "productID":"1ebfca5f-6b3a-413b-851f-b09c145817a2",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1ebfca5f-6b3a-413b-851f-b09c145817a2.jpg",
         "itemDetails":"uspn white shirt",
         "category":"shirt",
         "price":599,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":149,
         "productID":"1f89347d-3fe8-4e0e-853b-67c96c204c9e",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/1f89347d-3fe8-4e0e-853b-67c96c204c9e.jpg",
         "itemDetails":"peter england white shirt",
         "category":"shirt",
         "price":399,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":150,
         "productID":"2b3a5050-1533-4f69-a732-88e102b8e89d",
         "sellerDetails":"sjc retailers vittal malaya road,near vittal mallaya hospital,Bangalore",
         "sellerLocation":[
            12.969113,
            77.594641
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2b3a5050-1533-4f69-a732-88e102b8e89d.jpg",
         "itemDetails":"crocodile white shirt",
         "category":"shirt",
         "price":299,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":151,
         "productID":"2c042b2c-a3cf-42e2-bb29-5e6dbd408647",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2c042b2c-a3cf-42e2-bb29-5e6dbd408647.jpg",
         "itemDetails":"levis white shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":152,
         "productID":"2d38c37a-f31c-4715-8c22-2e7f45003236",
         "sellerDetails":"AB texttiles Manorayana palya,R.T.Nagar Post,Bangalore",
         "sellerLocation":[
            13.030062,
            77.606478
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/2d38c37a-f31c-4715-8c22-2e7f45003236.jpg",
         "itemDetails":"peter england white shirt",
         "category":"shirt",
         "price":989,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":153,
         "productID":"4bc3dd22-6229-4593-b978-747e59e372cf",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/4bc3dd22-6229-4593-b978-747e59e372cf.jpg",
         "itemDetails":"levis white shirt",
         "category":"shirt",
         "price":759,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":154,
         "productID":"5b9d766d-0ad8-41e2-8a2e-2b1227e871dc",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5b9d766d-0ad8-41e2-8a2e-2b1227e871dc.jpg",
         "itemDetails":"uspn white shirt",
         "category":"shirt",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":155,
         "productID":"5ddd23ad-e060-4e8a-a5ef-f7d3179567ff",
         "sellerDetails":"rockers store lal bagh road,Bangalore",
         "sellerLocation":[
            12.950828,
            77.584739
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/5ddd23ad-e060-4e8a-a5ef-f7d3179567ff.jpg",
         "itemDetails":"levis white shirt",
         "category":"shirt",
         "price":999,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":156,
         "productID":"6aafcce9-797e-46dd-852d-4e991aafe5ba",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6aafcce9-797e-46dd-852d-4e991aafe5ba.jpg",
         "itemDetails":"uspn white shirt",
         "category":"shirt",
         "price":500,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":157,
         "productID":"6da0a923-fa4c-4ef2-a679-4e398fe52122",
         "sellerDetails":"xyz Fashion chagalatti,Bagalur,near kempegowda airport,Bangalore",
         "sellerLocation":[
            13.117597,
            77.655401
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/6da0a923-fa4c-4ef2-a679-4e398fe52122.jpg",
         "itemDetails":"uspn white shirt",
         "category":"shirt",
         "price":599,
         "locationName":"bangalore",
         "sub_category":"white"
      },
      {
         "itemID":158,
         "productID":"7a327f00-0381-4ae9-990f-1030fc74334d",
         "sellerDetails":"maxx fashionz mcehs layout,Bangalore",
         "sellerLocation":[
            13.069917,
            77.62297
         ],
         "itemImageUrl":"https://hiiiiappservice.blob.core.windows.net/shopping-advisor/7a327f00-0381-4ae9-990f-1030fc74334d.jpg",
         "itemDetails":"roadster white shirt",
         "category":"shirt",
         "price":699,
         "locationName":"bangalore",
         "sub_category":"white"
      }
   ]
}))