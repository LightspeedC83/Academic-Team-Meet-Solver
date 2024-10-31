package New_Attempts_Java;

import java.util.ArrayList;
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

        //now we shall print the graph that we just made
        for(School x : schools){
            System.out.println(x.getName());
            for (School y : connections.outNeighbors(x)){
                System.out.println("\t"+y.getName()+" "+connections.getEdge(x, y));
            }
        }

        // TODO: make infrastructure to build the meet schedule and keep track of it as we whittle down the graph
    }
}
