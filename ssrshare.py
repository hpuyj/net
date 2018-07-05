# -*- coding: utf-8 -*-
import base64
import requests
import json
import pymysql
import os
from lxml import etree
from dingyue import encode_ssr,b64_encode,b64_decode
ssr_b={
"method": "",
"obfs": "plain",
"obfsparam": "",
"password": "",
"port": "",
"protocol": "origin",
"protoparam": "",
"server": "",
"remarks": "",
"group":"",
}
def ssrshare():
    num=0
    ssr={
    "method": "",
    "obfs": "plain",
    "obfsparam": "",
    "password": "",
    "port": "",
    "protocol": "origin",
    "protoparam": "",
    "server": "",
    "remarks": "",
    "group":""
    }
    free_ssr={
        "https://tool.ssrshare.xyz/tool/api/free_ssr?key=1529942400_8_xuo&page=1&limit=90",
        "https://tool.ssrshare.xyz/tool/api/share_ssr?key=1529942400_8_xuo&page=1&limit=90",
        }
    for url in free_ssr:
        r=requests.post(url)
        print(r.status_code)
        if r.status_code==200:
            happy = json.loads(r.text)
            result=happy['data']
            for x in result:
                # exit_code = os.system('ping '+x["server"])
                # if not exit_code:
                ssr["group"]="ssrshare"
                ssr["method"]=x["method"]
                ssr["obfs"]=x["obfs"]
                ssr["obfsparam"]=x["obfsparam"]
                ssr["password"]=x["password"]
                ssr["protocol"]=x["protocol"]
                ssr["protoparam"]=x["protocolparam"]
                ssr["remarks"]="ping"+str(x["m_station_cn_ms"])
                ssr["server"]=x["server"]
                ssr["port"]=int(x["server_port"])
                print(encode_ssr(ssr))
                ssr_Mysql(ssr)
                ssr=ssr_b
                num=num+1
                # else :
                #     print("ping 不通")
                #     num=num+1
    return num
    print(num)
def ishadowx():
    num=0
    ssr={
    "method": "",
    "obfs": "plain",
    "obfsparam": "",
    "password": "",
    "port": "",
    "protocol": "origin",
    "protoparam": "",
    "server": "",
    "remarks": "",
    "group":"",
    }
    url = 'https://my.ishadowx.net/'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = requests.get(url, headers=head)
    print(req.status_code)
    # print(req.text)
    html = etree.HTML(req.text)
    portfolio=html.xpath("//*[@id=\"portfolio\"]/div[2]/div[2]/div/div/div/div/div")
    for div in portfolio:
        ssr["group"]="ishadowx"
        ssr["remarks"]="ping"
        ssr["server"]=div.xpath("h4[1]/span[1]/text()")[0].replace("\n", "").replace(" ", "")
        ssr["port"]=div.xpath("h4[2]/span[1]/text()")[0].replace("\n", "").replace(" ", "")
        ssr["password"]=div.xpath("h4[3]/span[1]/text()")[0].replace("\n", "").replace(" ", "")
        ssr["method"]=div.xpath("h4[4]/text()")[0].replace("\n", "").replace(" ", "").replace("Method:", "")
        print(encode_ssr(ssr))
        ssr_Mysql(ssr)
        ssr=ssr_b
        num=num+1
    return num
    print(num)
def ssr_Mysql(ssr):
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1","root","kaixin88,,","ssr",charset='utf8' )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM `ssrshare` WHERE server='%s' AND port='%s' AND password='%s' AND method='%s'"% (ssr["server"],ssr["port"],ssr["password"],ssr["method"])
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if(len(results)!=0):
            print("数据库有相关数据，不进行写入")
        else:
            sql = """INSERT INTO `ssrshare` (`id`, `server`, `port`, `password`, `method`, `protocol`, `protoparam`, `obfs`, `obfsparam`, `remarks`, `group`) VALUES ('', '%s', '%d', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s')""" %  (ssr["server"], ssr["port"], ssr["password"], ssr["method"], ssr["protocol"], ssr["protoparam"], ssr["obfs"], ssr["obfsparam"], ssr["remarks"], ssr["group"])
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except Exception as e:
                # 如果发生错误则回滚
                print("发生异常",e)
                db.rollback()
                print("失败")
            
        # 关闭数据库连接
    except:
        print ("查找出现错误")
        # SQL 插入语句

    db.close()
def ping():
    ssr={
    "method": "",
    "obfs": "plain",
    "obfsparam": "",
    "password": "",
    "port": "",
    "protocol": "origin",
    "protoparam": "",
    "server": "",
    "remarks": "",
    "group":"",
    }
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1","root","kaixin88,,","ssr",charset='utf8' )
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM `ssrshare`"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for ssr_sql in results:
            ssr["server"]=ssr_sql[1]
            ssr["port"]=ssr_sql[1]
            ssr["password"]=ssr_sql[1]
            ssr["method"]=ssr_sql[1]
            ssr["protocol"]=ssr_sql[1]
            ssr["protoparam"]=ssr_sql[1]
            # ssr["obfs"], ssr["obfsparam"], ssr["remarks"], ssr["group"])       
            print("数据库有相关数据，不进行写入")
        else:
            sql = """INSERT INTO `ssrshare` (`id`, `server`, `port`, `password`, `method`, `protocol`, `protoparam`, `obfs`, `obfsparam`, `remarks`, `group`) VALUES ('', '%s', '%d', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s')""" %  (ssr["server"], ssr["port"], ssr["password"], ssr["method"], ssr["protocol"], ssr["protoparam"], ssr["obfs"], ssr["obfsparam"], ssr["remarks"], ssr["group"])
            try:
                # 执行sql语句
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except Exception as e:
                # 如果发生错误则回滚
                print("发生异常",e)
                db.rollback()
                print("失败")
            
        # 关闭数据库连接
    except:
        print ("查找出现错误")
        # SQL 插入语句

    db.close()    
def dingyue():
    url_list={
        "https://tool.ssrshare.xyz/tool/api/getGolSub?key=1530720000_7_eeo",
        "https://tool.ssrshare.xyz/tool/api/getCnSub?key=1530720000_7_eeo",
        "https://raw.githubusercontent.com/ImLaoD/sub/master/ssrshare.com",
        "http://share-shadowsocks.herokuapp.com/full/subscribe",
        # "http://share-shadowsocksr.herokuapp.com/subscribe?valid=1",
        "https://wxkxsw.com/link/yscIOaGChSaSfAQ0?mu=0",
        "https://prom-php.herokuapp.com/cloudfra_ssr.txt",

        }
    dy=""
    for url in url_list:
        try:
            r=requests.get(url)
            dy+=b64_decode(r.text)
        except:
            print("网页请求失败"+url)
    f = open("web.txt", "w+")
    f.write(b64_encode(b64_encode(dy)))
    f.close()
def main():
    # num=0
    # num=num+ssrshare()
    # num=num+ishadowx()
    # print(num)
    dingyue()

if __name__ == '__main__':
    main()