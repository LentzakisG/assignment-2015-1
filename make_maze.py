import random
import os, sys
n = int(input())
while n > 30:
        n = int(input());
start_x = int(input())
start_y = int(input())
seed = input()
output_file = input()
random.seed(seed)
graph = {};
visited = {};
for i in range(0,n):
        for j in range(0,n):
            visited.update({ (i,j) : False});
            if i == 0:
                if j == 0:
                    graph.update({ (i,j) : [(i+1,j) , (i,j+1)]});
                elif j == n-1:
                    graph.update({ (i,j) : [(i+1,j) , (i,j-1)]});
                else:
                    graph.update({ (i,j) : [(i+1,j) , (i,j+1) , (i,j-1)]});
            elif i == n-1:
                if j == 0:
                    graph.update({ (i,j) : [(i-1,j) , (i,j+1)]});
                elif j == n-1:
                    graph.update({ (i,j) : [(i-1,j) , (i,j-1)]});
                else:
                    graph.update({ (i,j) : [(i-1,j) , (i-1,j-1) , (i-1,j+1)]});
            elif j == 0:
                if i == 0:
                    graph.update({ (i,j) : [(i+1,j) , (i,j+1)]});
                elif i == n-1:
                    graph.update({ (i,j) : [(i-1,j) , (i,j+1)]});
                else:
                    graph.update({ (i,j) : [(i+1,j) , (i,j+1) , (i-1,j)]});
            elif j == n-1:
                if i == 0:
                    graph.update({ (i,j) : [(i+1,j) , (i,j-1)]});
                elif i == n-1:
                    graph.update({ (i,j) : [(i-1,j) , (i,j-1)]});
                else:
                    graph.update({ (i,j) : [(i-1,j) , (i,j-1) , (i+1,j)]});
            else:
                graph.update({ (i,j) : [(i+1,j) , (i,j+1) , (i-1,j) , (i,j-1)]})

fo = open(output_file,"w")
p = (start_x, start_y);
lon = [p];
lof = [];
while len(lon) != 0:
        while p in lon:
            while p not in lof:
                if not visited[p]:
                    lof.append(p);
                    lon.remove(p);
                    visited.update({ p : True});
                    lon.extend(graph[p]);
                    lon = [p for p in lon if p not in lof];
                    fo.write(str(p));
                    fo.write(', ');
                    if len(lon) != 0:
                        lon = random.sample(lon, len(lon));
                        p = lon[-1];
                    fo.write(str(p));
                    fo.write('\n');
fo.close();
readFile = open(output_file)
lines = readFile.readlines()
readFile.close()
w = open(output_file,'w')
w.writelines([item for item in lines[:-1]])
w.close()
