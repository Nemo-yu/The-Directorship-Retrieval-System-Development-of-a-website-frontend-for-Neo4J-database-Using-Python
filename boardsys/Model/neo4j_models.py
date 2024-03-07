from py2neo import Graph, NodeMatcher


class Neo4j_op():
    graph = None
    matcher = None

    def __init__(self):
        print('neo4j starting')

    def connect(self):
        self.graph = Graph('http://localhost:7474/', username='neo4j', password='hewenyu')
        self.matcher = NodeMatcher(self.graph)

    def matchname(self,names):
        namelist = names.split(',')
        answer = []
        for name in namelist:
            part = self.graph.run('match (f)-[r:Serve]->(t) <- [r1:Serve] - (f1) where f.name= \''+ name +'\'return f,r,t,r1,f1 limit 200')
            for i in part:
                answer.append(i)
        return answer

    def matchinstitution_uni(self,unis):
        unilist = unis.split(',')
        answer = []
        for name in unilist:
            part = self.graph.run('match (f) <- [r:Serve]  - (t) -[r1:Serve]-> (f1)  where f.uni= \''+ name +'\' match (f2) <- [r2:Serve]  - (t2) where f2.uni= \''+ name +'\' return f,r,t,r1,f1,f2,r2,t2 limit 200')
            for i in part:
                answer.append(i)
        return answer

    def matchinstitution_poly(self,polys):
        polylist = polys.split(',')
        answer = []
        for name in polylist:
            part = self.graph.run('match (f) <- [r:Serve]  - (t) -[r1:Serve]-> (f1)  where f.poly= \''+ name +'\' match (f2) <- [r2:Serve]  - (t2) where f2.poly= \''+ name +'\' return f,r,t,r1,f1,f2,r2,t2 limit 200')
            for i in part:
                answer.append(i)
        return answer
    
    def matchinstitution_tele(self,teles):
        telelist = teles.split(',')
        answer = []
        for name in telelist:
            part = self.graph.run('match (f) <- [r:Serve]  - (t) -[r1:Serve]-> (f1)  where f.tele= \''+ name +'\' match (f2) <- [r2:Serve]  - (t2) where f2.tele= \''+ name +'\' return f,r,t,r1,f1,f2,r2,t2 limit 200')
            for i in part:
                answer.append(i)
        return answer

    def matchinstitution_misc(self,miscs):
        misclist = miscs.split(',')
        answer = []
        for name in misclist:
            part = self.graph.run('match (f) <- [r:Serve]  - (t) -[r1:Serve]-> (f1)  where f.misc= \''+ name +'\' match (f2) <- [r2:Serve]  - (t2) where f2.misc= \''+ name +'\' return f,r,t,r1,f1,f2,r2,t2 limit 200')
            for i in part:
                answer.append(i)
        return answer

    def matchinstitution_go(self,gos):
        golist = gos.split(',')
        answer = []
        for name in golist:
            part = self.graph.run('match (f) <- [r:Serve]  - (t) -[r1:Serve]-> (f1)  where f.go= \''+ name +'\' match (f2) <- [r2:Serve]  - (t2) where f2.go= \''+ name +'\' return f,r,t,r1,f1,f2,r2,t2 limit 200')
            for i in part:
                answer.append(i)
        return answer

    def matchinstitution_legal(self,legals):
        legallist = legals.split(',')
        answer = []
        for name in legallist:
            part = self.graph.run('match (f) <- [r:Serve]  - (t) -[r1:Serve]-> (f1)  where f.legal= \''+ name +'\' match (f2) <- [r2:Serve]  - (t2) where f2.legal= \''+ name +'\' return f,r,t,r1,f1,f2,r2,t2 limit 200')
            for i in part:
                answer.append(i)
        return answer

    def matchinstitution_sti(self,stis):
        stilist = stis.split(',')
        answer = []
        for name in stilist:
            part = self.graph.run('match (f) <- [r:Serve]  - (t) -[r1:Serve]-> (f1)  where f.sti= \''+ name +'\' match (f2) <- [r2:Serve]  - (t2) where f2.sti= \''+ name +'\' return f,r,t,r1,f1,f2,r2,t2 limit 200')
            for i in part:
                answer.append(i)
        return answer
