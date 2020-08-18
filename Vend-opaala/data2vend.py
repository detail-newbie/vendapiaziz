import psycopg2
import requests
import json

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "admin",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"n")

    test = "debug 1"
    # Print PostgreSQL version
 #Sql query given below for extracting data from postgres but for now i am not sending the data in vend because of syncronization of vend with Opaala
    query = ("select o.id OrderId,o.status as OrderStatus, o.created_at ordercreatedDate,o.user_id, o.total_price ordertotalprice "
                   "  ,oi.id lineid,di.name itemname, di.description itemDescription, "
                   " oi.quantity, oi.unit_price, oi.total_price linetotalprice ,oi.item_id "
                   " , r.tablename, r.restaurantname "
                   " ,n.description noticationDescription, n.comment notificationcomment, n.status notificationstatus, "
                   " n.type notificationtype , r.resturantid" 
               "  from order_order o "
                "    INNER JOIN order_orderitem oi ON o.id=oi.order_id  "
                 "   INNER JOIN (select dt.id tableid, dt.name tablename, dr.name restaurantname, dr.id resturantid "
                  "              from  data_table dt inner join data_restaurant dr "
                   "             on DT.restaurant_id = dr.id "
                     "           ) as r "
                      "          ON o.table_id=r.tableid  "
                   " INNER JOIN data_item di on oi.item_id = di.id  "
                   " INNER JOIN notification_notification as n on o.id = n.order_id ")
    cursor.execute(query)
    test = "debug 2"
    OrderDataSet = cursor.fetchone()
    test = "debug 3"
    url = "https://sohailtest.vendhq.com/api/register_sales"
      
    headers = {
                'Authorization': "Bearer 4GYI1hpMtzRwTjUO7cBox_pv7HZZ3Pehag0HXTSw",
                 'Content-Type': 'application/json',
             }
    test = "debug 4"
    
    
    
#debug no.s identify if there is any mistake it shows while printing that in what line error occurs

    fil = { "register_id": "0242e39e-bfda-11ea-fc6f-dbf77b701099" , "user_id": "0242e39e-bfda-11ea-fc6f-dbf77b7257df", "status": "SAVED", "register_sale_products":[{ "product_id": "0242e39e-bf27-11ea-fc6f-dbf77c49a555", "quantity": 1,"price": 12, "tax": 1.8, "tax_id": "0242e39e-bfda-11ea-fc6f-dbf77b61f49f"}]}


    test = "debug 5"
    print(fil)
    response = requests.request("POST", url, headers=headers, data = json.dumps(fil))

    print (response.status_code)
    print(response.text)
    test = "debug 6"


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL "+test +" ", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
  
     
            
            
            
            

