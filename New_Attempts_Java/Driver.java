package New_Attempts_Java;

import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;


public class Driver {
    public static void main(String[] args) throws Exception {
        // creating a bunch of school objects with the proper identificaiton information
        String[] schoolNames = new String[]{"RCHS","SHS","BHS","RHS","HHS","TAHS","ERHS","WMHS"};
        ArrayList<School> schools = new ArrayList<>(); 
        for (int i=0; i<8; i++){
            schools.add(new School(schoolNames[i], i));
        }

        // setting up a graph that will model the connections between the schools
        // this will model the final state after all the meets, we will take this and work backwards
        // Each node is a school object, edges between nodes represent the schools' A teams playing each other
        SimpleAdjacencyMap<School, Integer> connections = new SimpleAdjacencyMap<>();
        for (School school : schools){
            connections.insertVertex(school);
        }
        for (School school : schools){
            for (School other : schools){
                if (school != other){
                    connections.insertUndirected(school, other,2);
                }
            }
        }

        // //now we shall print the graph that we just made and the nodes' connections
        // for(School x : schools){
        //     System.out.println(x.getName());
        //     for (School y : connections.outNeighbors(x)){
        //         System.out.println("\t"+y.getName()+" "+connections.getEdge(x, y));
        //     }
        // }

        // TODO: make infrastructure to build the meet schedule and keep track of it as we whittle down the graph
        // creating a meet schedule that we will build up as we go
        ArrayList<ArrayList<ArrayList<School>>> meetSchedule = new ArrayList<>();

        for(int i=0; i<7; i++){ //for each meet in the schedule
            //create a list with all the schools in it in a random order
            ArrayList<School> potentials = new ArrayList<>();
            for (School s : schools){
                potentials.add(s);
                s.resetMatchupsLeft();; //reset's schools exhaustion
            }
            Collections.shuffle(potentials);
            
            // adding one school to the meet half draft then adding two of it's neighbors
            ArrayList<School> meetOne = new ArrayList<>();
            
            // the school that we add will be a school with the highest out degree, using a priority queue to find that school
            PriorityQueue<School> pq = new PriorityQueue<>((s1, s2) -> Integer.compare(connections.outDegree(s2), connections.outDegree(s1)));
            for (School s : potentials){pq.add(s);}
            meetOne.add(pq.remove());
            potentials.remove(meetOne.get(0));
            
            int initAdd = 2;
            for (School x : connections.outNeighbors(meetOne.getFirst())){
                if(initAdd<=0){break;}
                else if (potentials.contains(x) && connections.getEdge(x, meetOne.getFirst())==2){ 
                    meetOne.add(x); 
                    potentials.remove(x);
                    initAdd--;
                }
            }
            //extra step now to fill out two initial matches for first school added to meetOne becuase the first pass focused on candidates with edge weight 2
            if (meetOne.size() != initAdd+1){ 
                int extraAdd = initAdd+1 - meetOne.size();
                for (School x : connections.outNeighbors(meetOne.getFirst())){
                    if(extraAdd<=0){break;}
                    else if (potentials.contains(x)){ // this check may be redundant, but i don't think it's hurting anyone
                        meetOne.add(x); 
                        potentials.remove(x);
                        extraAdd--;
                    }
                }
            }

            //now we add neighbors of the neighbors we just added to the meet half draft
            int extra = 1;
            // if(i<=1){extra=2;} // for the first two rounds we want to start with 5 schools in meetOne //TODO: <--address this
            for (int n=1; n<meetOne.size(); n++){
                School nextFocus = meetOne.get(n);
                for(School x :connections.outNeighbors(nextFocus)){
                    if (extra<=0){break;}
                    else if(potentials.contains(x) && connections.getEdge(x, nextFocus)==2){ // first pass with focus on neighbors with edge weight 2
                        meetOne.add(x);
                        potentials.remove(x);
                        extra--;
                    }
                }
                if(extra<=0){break;} 
            }
            //doing a second sweep for initialiing the list
            for (School x : connections.outNeighbors(meetOne.get(1))){ //going through the neighbors of one of the other two schools we added
                if (extra<=0){break;}
                else if(potentials.contains(x)){ // first pass with focus on neighbors with edge weight 2
                    meetOne.add(x);
                    potentials.remove(x);
                    extra--;
                }
            }
            
            
            // now we shall update the graph of the nodes in meetOne by whittling down the connections
            for (int s=0; s<meetOne.size(); s++){
                School current = meetOne.get(s);
                for (int o=0; o<meetOne.size(); o++){
                    if (o!=s){
                        School other = meetOne.get(o);
                        if (!current.getCurrentMatchupsExhausted() && !other.getCurrentMatchupsExhausted() && connections.hasEdge(other, current)){
                            //decrement connection strength or get rid of connection, decrement matchups left of each school
                            if (connections.getEdge(current, other) == 2){
                                connections.insertUndirected(current, other, 1);
                            } else if (connections.getEdge(current, other) ==1){
                                connections.removeUndirected(current, other);
                            }

                            current.decrementMatchupsLeft();
                            other.decrementMatchupsLeft();
                        }
                    }
                }
            }

            // now we update the connections of all the nodes remaining in the potentials list
            for (int s=0; s<potentials.size(); s++){
                School current = potentials.get(s);
                for (int o=0; o<potentials.size(); o++){
                    if (o!=s){
                        School other = potentials.get(o);
                        if (!current.getCurrentMatchupsExhausted() && !other.getCurrentMatchupsExhausted() && connections.hasEdge(other, current)){
                            if (connections.getEdge(current, other) == 2){
                                connections.insertUndirected(current, other, 1);
                            } else if (connections.getEdge(current, other) == 1){
                                connections.removeUndirected(current, other);
                            }

                            current.decrementMatchupsLeft();
                            other.decrementMatchupsLeft();
                        }
                    }
                }
            }
            
            //adding meetOne to the meet schedule and adding the other schools the other matchup in that round of the meet schedule
            ArrayList<ArrayList<School>> toAdd = new ArrayList<>();
            toAdd.add(meetOne);
            toAdd.add(potentials);
            meetSchedule.add(toAdd);
        }

        //printing the meet schedule
        int i = 0;
        for (ArrayList<ArrayList<School>> meet : meetSchedule){
            i++;
            System.out.println("meet: "+i);
            for (ArrayList<School> matchup : meet){
                System.out.print("\t");
                for(School s : matchup){
                    System.out.print(s.getName()+", ");
                }
                System.out.println("");
            }
        }
        
        System.out.println("\nconnections remaining:");
        //printing all the connections in the graph
        for(School x : schools){
            System.out.println(x.getName());
            for (School y : connections.outNeighbors(x)){
                System.out.println("\t"+y.getName()+" "+connections.getEdge(x, y));
            }
        }


    }
}
