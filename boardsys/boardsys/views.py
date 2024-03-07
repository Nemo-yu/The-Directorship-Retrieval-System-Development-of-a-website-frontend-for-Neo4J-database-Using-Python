from django.shortcuts import render
import Model.neo4j_models as neo4j
import json


def searchname(request):   #改了方法名
    if (request.GET):
        query = request.GET['name'] #改了column名,对应数据库
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchname(query) #改了方法名,对应佳益修改的方法
        if len(answer) != 0:
            inf = []
            list = []
            nodes = []
            links = []
            #print(answer)
            
            #symbolSize可以控制图形的大小，鉴于数据不多，全部放大了，不够再调；des应该就是标签
            for rel in answer:
                if 'name' in rel['f']:
                    if rel['f']['name'] not in list:
                        node = {'category': 0, 'name': rel['f']['name'], 'symbolSize': 80, 'des': 'Name'}
                        nodes.append(node)
                        list.append(rel['f']['name'])
                        #print("yyyyyyy")确定有
                if 'go' in rel['t'] and rel['t']['go'] not in list:
                    node = {'category': 1, 'name':rel['t']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['t']['go'])
                if 'legal' in rel['t'] and rel['t']['legal'] not in list:
                    node = {'category': 2, 'name': rel['t']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['t']['legal'])
                if 'misc' in rel['t'] and rel['t']['misc'] not in list:
                    node = {'category': 3, 'name': rel['t']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['t']['misc'])
                if 'poly' in rel['t'] and rel['t']['poly'] not in list:
                    node = {'category': 4, 'name': rel['t']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['t']['poly'])
                if 'sti' in rel['t'] and rel['t']['sti'] not in list:
                    node = {'category': 5, 'name': rel['t']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['t']['sti'])
                if 'tele' in rel['t'] and rel['t']['tele'] not in list:
                    node = {'category': 6, 'name': rel['t']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['t']['tele'])
                if 'uni' in rel['t'] and rel['t']['uni'] not in list:
                    node = {'category': 7, 'name': rel['t']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['t']['uni'])
                
            #这部分只改标签，source和target表示的是两个关联节点
                if 'go' in rel['t'] and 'name' in rel['f']:
                    link = {'source': rel['f']['name'], 'target': rel['t']['go'], 'name': 'Serve'}
                    links.append(link)
                if 'legal' in rel['t'] and 'name' in rel['f']:
                    link = {'source': rel['f']['name'], 'target': rel['t']['legal'], 'name': 'Serve'}
                    links.append(link)
                if 'misc' in rel['t'] and 'name' in rel['f']:
                    link = {'source': rel['f']['name'], 'target': rel['t']['misc'], 'name': 'Serve'}
                    links.append(link)
                if 'poly' in rel['t'] and 'name' in rel['f']:
                    link = {'source': rel['f']['name'], 'target': rel['t']['poly'], 'name': 'Serve'}
                    links.append(link)
                if 'sti' in rel['t'] and 'name' in rel['f']:
                    link = {'source': rel['f']['name'], 'target': rel['t']['sti'], 'name': 'Serve'}
                    links.append(link)
                if 'tele' in rel['t'] and 'name' in rel['f']:
                    link = {'source': rel['f']['name'], 'target': rel['t']['tele'], 'name': 'Serve'}
                    links.append(link)
                if 'uni' in rel['t'] and 'name' in rel['f']:
                    link = {'source': rel['f']['name'], 'target': rel['t']['uni'], 'name': 'Serve'}
                    links.append(link)

         
                
                        
            for rel in answer:
                if 'name' in rel['f1']:
                    if rel['f1']['name'] not in list:
                        node = {'category': 0, 'name': rel['f1']['name'], 'symbolSize': 80, 'des': 'Name'}
                        nodes.append(node)
                        list.append(rel['f1']['name'])
            #这部分只改标签，source和target表示的是两个关联节点
                if 'go' in rel['t'] and 'name' in rel['f1']:
                    link = {'source': rel['f1']['name'], 'target': rel['t']['go'], 'name': 'Serve'}
                    links.append(link)
                if 'legal' in rel['t'] and 'name' in rel['f1']:
                    link = {'source': rel['f1']['name'], 'target': rel['t']['legal'], 'name': 'Serve'}
                    links.append(link)
                if 'misc' in rel['t'] and 'name' in rel['f1']:
                    link = {'source': rel['f1']['name'], 'target': rel['t']['misc'], 'name': 'Serve'}
                    links.append(link)
                if 'poly' in rel['t'] and 'name' in rel['f1']:
                    link = {'source': rel['f1']['name'], 'target': rel['t']['poly'], 'name': 'Serve'}
                    links.append(link)
                if 'sti' in rel['t'] and 'name' in rel['f1']:
                    link = {'source': rel['f1']['name'], 'target': rel['t']['sti'], 'name': 'Serve'}
                    links.append(link)
                if 'tele' in rel['t'] and 'name' in rel['f1']:
                    link = {'source': rel['f1']['name'], 'target': rel['t']['tele'], 'name': 'Serve'}
                    links.append(link)
                if 'uni' in rel['t'] and 'name' in rel['f1']:
                    link = {'source': rel['f1']['name'], 'target': rel['t']['uni'], 'name': 'Serve'}
                    links.append(link)
                
            
            return render(request, 'search_name.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_name.html', {'searchresult': 'The person not found'})
    return render(request, 'search_name.html', {'searchresult': ''})


def searchuni(request):
    if (request.GET):
        query = request.GET['uni']
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchinstitution_uni(query)
        if len(answer) != 0:
            list = []
            nodes = []
            links = []
            #print(answer)
            for rel in answer:
                if rel['f']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f']['uni'], 'symbolSize': 80, 'des': 'University'}
                    list.append(rel['f']['uni'])
                    nodes.append(node)
                
                if rel['t']['name'] not in list:
                    node = {'category': 0, 'name': rel['t']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t']['name'])
                    nodes.append(node)
                    link = {'source': rel['t']['name'], 'target':rel['f']['uni'] , 'name': 'Serve'}
                    links.append(link)
                
                if 'go' in rel['f1'] and rel['f1']['go'] not in list:
                    node = {'category': 1, 'name':rel['f1']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['f1']['go'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['go'], 'name': 'Serve'}
                    links.append(link2)
                if 'legal' in rel['f1'] and rel['f1']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f1']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['f1']['legal'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['legal'], 'name': 'Serve'}
                    links.append(link2)
                if 'misc' in rel['f1'] and rel['f1']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f1']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['f1']['misc'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['misc'], 'name': 'Serve'}
                    links.append(link2)
                if 'poly' in rel['f1'] and rel['f1']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f1']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['f1']['poly'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['poly'], 'name': 'Serve'}
                    links.append(link2)
                if 'sti' in rel['f1'] and rel['f1']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f1']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['f1']['sti'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['sti'], 'name': 'Serve'}
                    links.append(link2)
                if 'tele' in rel['f1'] and rel['f1']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f1']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['f1']['tele'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['tele'], 'name': 'Serve'}
                    links.append(link2)
                if 'uni' in rel['f1'] and rel['f1']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f1']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['f1']['uni'])
                    link2 = {'source':rel['t']['name'], 'target':  rel['f1']['uni'], 'name': 'Serve'}
                    links.append(link2)
                    #print('okokokokoko')
            
                if rel['t2']['name'] not in list:
                    node = {'category': 0, 'name': rel['t2']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t2']['name'])
                    nodes.append(node)
                    link3 = {'source':rel['t2']['name'] , 'target': rel['f']['uni'], 'name': 'Serve'}
                    links.append(link3)
                
                
            #print(nodes)
            #print(links)
                
            
            return render(request, 'search_uni.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_uni.html', {'searchresult': 'University not found'})
    return render(request, 'search_uni.html', {'searchresult': ''})


def searchpoly(request):
    if (request.GET):
        query = request.GET['poly']
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchinstitution_poly(query)
        if len(answer) != 0:
            list = []
            nodes = []
            links = []
            for rel in answer:
                
                if rel['f']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    list.append(rel['f']['poly'])
                    nodes.append(node)
                if rel['t']['name'] not in list:
                    node = {'category': 0, 'name': rel['t']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t']['name'])
                    nodes.append(node)
                    link = {'source':rel['t']['name'] , 'target': rel['f']['poly'], 'name': 'Serve'}
                    links.append(link)
                if 'go' in rel['f1'] and rel['f1']['go'] not in list:
                    node = {'category': 1, 'name':rel['f1']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['f1']['go'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['go'], 'name': 'Serve'}
                    links.append(link2)
                if 'legal' in rel['f1'] and rel['f1']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f1']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['f1']['legal'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['legal'], 'name': 'Serve'}
                    links.append(link2)
                if 'misc' in rel['f1'] and rel['f1']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f1']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['f1']['misc'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['misc'], 'name': 'Serve'}
                    links.append(link2)
                if 'poly' in rel['f1'] and rel['f1']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f1']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['f1']['poly'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['poly'], 'name': 'Serve'}
                    links.append(link2)
                if 'sti' in rel['f1'] and rel['f1']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f1']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['f1']['sti'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['sti'], 'name': 'Serve'}
                    links.append(link2)
                if 'tele' in rel['f1'] and rel['f1']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f1']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['f1']['tele'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['tele'], 'name': 'Serve'}
                    links.append(link2)
                if 'uni' in rel['f1'] and rel['f1']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f1']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['f1']['uni'])
                    link2 = {'source':rel['t']['name'], 'target':  rel['f1']['uni'], 'name': 'Serve'}
                    links.append(link2)
                if rel['t2']['name'] not in list:
                    node = {'category': 0, 'name': rel['t2']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t2']['name'])
                    nodes.append(node)
                    link3 = {'source': rel['t2']['name'], 'target': rel['f']['poly'], 'name': 'Serve'}
                    links.append(link3)
                
                
                
                
            return render(request, 'search_poly.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_poly.html', {'searchresult': 'Polytechnic not found'})
    return render(request, 'search_poly.html', {'searchresult': ''})


def searchtele(request):
    if (request.GET):
        query = request.GET['tele']
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchinstitution_tele(query)
        if len(answer) != 0:
            list = []
            nodes = []
            links = []
            for rel in answer:
                if rel['f']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    list.append(rel['f']['tele'])
                    nodes.append(node)
                if rel['t']['name'] not in list:
                    node = {'category': 0, 'name': rel['t']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t']['name'])
                    nodes.append(node)
                    link = {'source': rel['t']['name'], 'target':rel['f']['tele'] , 'name': 'Serve'}
                    links.append(link)
                if 'go' in rel['f1'] and rel['f1']['go'] not in list:
                    node = {'category': 1, 'name':rel['f1']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['f1']['go'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['go'], 'name': 'Serve'}
                    links.append(link2)
                if 'legal' in rel['f1'] and rel['f1']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f1']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['f1']['legal'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['legal'], 'name': 'Serve'}
                    links.append(link2)
                if 'misc' in rel['f1'] and rel['f1']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f1']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['f1']['misc'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['misc'], 'name': 'Serve'}
                    links.append(link2)
                if 'poly' in rel['f1'] and rel['f1']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f1']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['f1']['poly'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['poly'], 'name': 'Serve'}
                    links.append(link2)
                if 'sti' in rel['f1'] and rel['f1']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f1']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['f1']['sti'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['sti'], 'name': 'Serve'}
                    links.append(link2)
                if 'tele' in rel['f1'] and rel['f1']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f1']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['f1']['tele'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['tele'], 'name': 'Serve'}
                    links.append(link2)
                if 'uni' in rel['f1'] and rel['f1']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f1']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['f1']['uni'])
                    link2 = {'source':rel['t']['name'], 'target':  rel['f1']['uni'], 'name': 'Serve'}
                    links.append(link2)
                if rel['t2']['name'] not in list:
                    node = {'category': 0, 'name': rel['t2']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t2']['name'])
                    nodes.append(node)
                    link3 = {'source': rel['t2']['name'], 'target':rel['f']['tele'] , 'name': 'Serve'}
                    links.append(link3)
                
                
                
                
            return render(request, 'search_tele.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_tele.html', {'searchresult': 'University not found'})
    return render(request, 'search_tele.html', {'searchresult': ''})


def searchmisc(request):
    if (request.GET):
        query = request.GET['misc']
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchinstitution_misc(query)
        if len(answer) != 0:
            list = []
            nodes = []
            links = []
            for rel in answer:
                if rel['f']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    list.append(rel['f']['misc'])
                    nodes.append(node)
                if rel['t']['name'] not in list:
                    node = {'category': 0, 'name': rel['t']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t']['name'])
                    nodes.append(node)
                    link = {'source':rel['t']['name'] , 'target': rel['f']['misc'], 'name': 'Serve'}
                    links.append(link)
                if 'go' in rel['f1'] and rel['f1']['go'] not in list:
                    node = {'category': 1, 'name':rel['f1']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['f1']['go'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['go'], 'name': 'Serve'}
                    links.append(link2)
                if 'legal' in rel['f1'] and rel['f1']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f1']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['f1']['legal'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['legal'], 'name': 'Serve'}
                    links.append(link2)
                if 'misc' in rel['f1'] and rel['f1']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f1']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['f1']['misc'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['misc'], 'name': 'Serve'}
                    links.append(link2)
                if 'poly' in rel['f1'] and rel['f1']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f1']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['f1']['poly'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['poly'], 'name': 'Serve'}
                    links.append(link2)
                if 'sti' in rel['f1'] and rel['f1']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f1']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['f1']['sti'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['sti'], 'name': 'Serve'}
                    links.append(link2)
                if 'tele' in rel['f1'] and rel['f1']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f1']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['f1']['tele'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['tele'], 'name': 'Serve'}
                    links.append(link2)
                if 'uni' in rel['f1'] and rel['f1']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f1']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['f1']['uni'])
                    link2 = {'source':rel['t']['name'], 'target':  rel['f1']['uni'], 'name': 'Serve'}
                    links.append(link2)
                if rel['t2']['name'] not in list:
                    node = {'category': 0, 'name': rel['t2']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t2']['name'])
                    nodes.append(node)
                    link3 = {'source':rel['t2']['name'], 'target':  rel['f']['misc'], 'name': 'Serve'}
                    links.append(link3)
                
               
               
                
            return render(request, 'search_misc.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_misc.html', {'searchresult': 'Misc not found'})
    return render(request, 'search_misc.html', {'searchresult': ''})

def searchgo(request):
    if (request.GET):
        query = request.GET['go']
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchinstitution_go(query)
        if len(answer) != 0:
            list = []
            nodes = []
            links = []
            for rel in answer:
                if rel['f']['go'] not in list:
                    node = {'category': 1, 'name': rel['f']['go'], 'symbolSize': 80, 'des': 'Government_Organisation'}
                    list.append(rel['f']['go'])
                    nodes.append(node)
                if rel['t']['name'] not in list:
                    node = {'category': 0, 'name': rel['t']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t']['name'])
                    nodes.append(node)
                    link = {'source':rel['t']['name'] , 'target':rel['f']['go'] , 'name': 'Serve'}
                    links.append(link)
                if 'go' in rel['f1'] and rel['f1']['go'] not in list:
                    node = {'category': 1, 'name':rel['f1']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['f1']['go'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['go'], 'name': 'Serve'}
                    links.append(link2)
                if 'legal' in rel['f1'] and rel['f1']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f1']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['f1']['legal'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['legal'], 'name': 'Serve'}
                    links.append(link2)
                if 'misc' in rel['f1'] and rel['f1']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f1']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['f1']['misc'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['misc'], 'name': 'Serve'}
                    links.append(link2)
                if 'poly' in rel['f1'] and rel['f1']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f1']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['f1']['poly'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['poly'], 'name': 'Serve'}
                    links.append(link2)
                if 'sti' in rel['f1'] and rel['f1']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f1']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['f1']['sti'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['sti'], 'name': 'Serve'}
                    links.append(link2)
                if 'tele' in rel['f1'] and rel['f1']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f1']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['f1']['tele'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['tele'], 'name': 'Serve'}
                    links.append(link2)
                if 'uni' in rel['f1'] and rel['f1']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f1']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['f1']['uni'])
                    link2 = {'source':rel['t']['name'], 'target':  rel['f1']['uni'], 'name': 'Serve'}
                    links.append(link2)
                if rel['t2']['name'] not in list:
                    node = {'category': 0, 'name': rel['t2']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t2']['name'])
                    nodes.append(node)
                    link3 = {'source':rel['t2']['name'] , 'target': rel['f']['go'], 'name': 'Serve'}
                    links.append(link3)
                
                
               
                
            return render(request, 'search_go.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_go.html', {'searchresult': 'Government_Organisation not found'})
    return render(request, 'search_go.html', {'searchresult': ''})

def searchlegal(request):
    if (request.GET):
        query = request.GET['legal']
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchinstitution_legal(query)
        if len(answer) != 0:
            list = []
            nodes = []
            links = []
            for rel in answer:
                if rel['f']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f']['legal'], 'symbolSize': 80, 'des': 'Legal_Institution'}
                    list.append(rel['f']['legal'])
                    nodes.append(node)
                if rel['t']['name'] not in list:
                    node = {'category': 0, 'name': rel['t']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t']['name'])
                    nodes.append(node)
                    link = {'source': rel['t']['name'], 'target': rel['f']['legal'], 'name': 'Serve'}
                    links.append(link)
                if 'go' in rel['f1'] and rel['f1']['go'] not in list:
                    node = {'category': 1, 'name':rel['f1']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['f1']['go'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['go'], 'name': 'Serve'}
                    links.append(link2)
                if 'legal' in rel['f1'] and rel['f1']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f1']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['f1']['legal'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['legal'], 'name': 'Serve'}
                    links.append(link2)
                if 'misc' in rel['f1'] and rel['f1']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f1']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['f1']['misc'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['misc'], 'name': 'Serve'}
                    links.append(link2)
                if 'poly' in rel['f1'] and rel['f1']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f1']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['f1']['poly'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['poly'], 'name': 'Serve'}
                    links.append(link2)
                if 'sti' in rel['f1'] and rel['f1']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f1']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['f1']['sti'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['sti'], 'name': 'Serve'}
                    links.append(link2)
                if 'tele' in rel['f1'] and rel['f1']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f1']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['f1']['tele'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['tele'], 'name': 'Serve'}
                    links.append(link2)
                if 'uni' in rel['f1'] and rel['f1']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f1']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['f1']['uni'])
                    link2 = {'source':rel['t']['name'], 'target':  rel['f1']['uni'], 'name': 'Serve'}
                    links.append(link2)
                if rel['t2']['name'] not in list:
                    node = {'category': 0, 'name': rel['t2']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t2']['name'])
                    nodes.append(node)
                    link3 = {'source': rel['t2']['name'], 'target': rel['f']['legal'], 'name': 'Serve'}
                    links.append(link3)
                
                
            return render(request, 'search_legal.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_legal.html', {'searchresult': 'Legal_Institution not found'})
    return render(request, 'search_legal.html', {'searchresult': ''})

def searchsti(request):
    if (request.GET):
        query = request.GET['sti']
        db = neo4j.Neo4j_op()
        db.connect()
        answer = db.matchinstitution_sti(query)
        if len(answer) != 0:
            list = []
            nodes = []
            links = []
            for rel in answer:
                if rel['f']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    list.append(rel['f']['sti'])
                    nodes.append(node)
                if rel['t']['name'] not in list:
                    node = {'category': 0, 'name': rel['t']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t']['name'])
                    nodes.append(node)
                    link = {'source':rel['t']['name'] , 'target':rel['f']['sti'] , 'name': 'Serve'}
                    links.append(link)
                if 'go' in rel['f1'] and rel['f1']['go'] not in list:
                    node = {'category': 1, 'name':rel['f1']['go'], 'symbolSize': 80, 'des':'Government_Organisation'}
                    nodes.append(node)
                    list.append(rel['f1']['go'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['go'], 'name': 'Serve'}
                    links.append(link2)
                if 'legal' in rel['f1'] and rel['f1']['legal'] not in list:
                    node = {'category': 2, 'name': rel['f1']['legal'], 'symbolSize': 80, 'des': 'Legal_institution'}
                    nodes.append(node)
                    list.append(rel['f1']['legal'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['legal'], 'name': 'Serve'}
                    links.append(link2)
                if 'misc' in rel['f1'] and rel['f1']['misc'] not in list:
                    node = {'category': 3, 'name': rel['f1']['misc'], 'symbolSize': 80, 'des': 'Misc'}
                    nodes.append(node)
                    list.append(rel['f1']['misc'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['misc'], 'name': 'Serve'}
                    links.append(link2)
                if 'poly' in rel['f1'] and rel['f1']['poly'] not in list:
                    node = {'category': 4, 'name': rel['f1']['poly'], 'symbolSize': 80, 'des': 'Polytechnic'}
                    nodes.append(node)
                    list.append(rel['f1']['poly'])
                    link2 = {'source': rel['t']['name'], 'target': rel['f1']['poly'], 'name': 'Serve'}
                    links.append(link2)
                if 'sti' in rel['f1'] and rel['f1']['sti'] not in list:
                    node = {'category': 5, 'name': rel['f1']['sti'], 'symbolSize': 80, 'des': 'STI'}
                    nodes.append(node)
                    list.append(rel['f1']['sti'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['sti'], 'name': 'Serve'}
                    links.append(link2)
                if 'tele' in rel['f1'] and rel['f1']['tele'] not in list:
                    node = {'category': 6, 'name': rel['f1']['tele'], 'symbolSize': 80, 'des': 'Telecommunication'}
                    nodes.append(node)
                    list.append(rel['f1']['tele'])
                    link2 = {'source':rel['t']['name'] , 'target': rel['f1']['tele'], 'name': 'Serve'}
                    links.append(link2)
                if 'uni' in rel['f1'] and rel['f1']['uni'] not in list:
                    node = {'category': 7, 'name': rel['f1']['uni'], 'symbolSize': 80, 'des': 'University'}
                    nodes.append(node)
                    list.append(rel['f1']['uni'])
                    link2 = {'source':rel['t']['name'], 'target':  rel['f1']['uni'], 'name': 'Serve'}
                    links.append(link2)
                if rel['t2']['name'] not in list:
                    node = {'category': 0, 'name': rel['t2']['name'], 'symbolSize': 80, 'des': 'Name'}
                    list.append(rel['t2']['name'])
                    nodes.append(node)
                    link3 = {'source': rel['t2']['name'], 'target': rel['f']['sti'], 'name': 'Serve'}
                    links.append(link3)
               
               
               
                
            return render(request, 'search_sti.html', {'nodes': json.dumps(nodes), 'links': json.dumps(links)})
        else:
            return render(request, 'search_sti.html', {'searchresult': 'STI not found'})
    return render(request, 'search_sti.html', {'searchresult': ''})


def home(request):
    return render(request, 'home.html')
