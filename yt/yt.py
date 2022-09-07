from pytube import YouTube
import os
import sqlite3


def down(indir,id):
    
    try:
    
     
        yt = YouTube(indir)
        #print(yt.description)
        cozunurluk = kalite()
        stat = yt.title
        
        yt.streams.filter(res=cozunurluk).first().download('Downloads')

        """
        my_video = youtube.streams.first()

        my_video.download('~/Downloads')        
        """
        #stream = yt.streams.get_by_itag(22)
        #stream.download()
       
        update(id,stat)
       # print("ok.")

    except:
        print("")


def kalite():
    try:

        conn = sqlite3.connect('deneme.db')
        cursor = conn.cursor()
        
        query = "select * FROM kalite where id = 1"
        cursor.execute(query)
    
        records = cursor.fetchall()
        #print("Total rows are:  ", len(records))
        for row in records:
            gidenkalite = row[1]
       

        cursor.close()    
        return gidenkalite

    except:
        print("")





def update(id, stat):

    try:
        conn = sqlite3.connect('deneme.db')
        cursor = conn.cursor()
        sql = "Update data set stat = ? where id = ?"
        data = (stat, id)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)








try:
   
    conn = sqlite3.connect('deneme.db')
    cursor = conn.cursor()
    
    query = "select * FROM data where stat like '0'"
    cursor.execute(query)
   
    records = cursor.fetchall()
    #print("Total rows are:  ", len(records))
    for row in records:
       # print("Start...")
        down(row[1],row[0])

    cursor.close()    
    


except sqlite3.Error as error:
    print(error)    






