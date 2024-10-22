package New_Attempts_Java;

import java.util.ArrayList;
public class Driver {
    public static void main(String[] args) {
        // creating a bunch of school objects with the proper identificaiton information
        String[] schoolNames = new String[]{"RCHS","SHS","BHS","RHS","HHS","TAHS","ERHS","WMHS"};
        ArrayList<School> schools = new ArrayList<>(); 
        for (int i=0; i<8; i++){
            schools.add(new School(schoolNames[i], i));
        }

        // setting up a graph that will model the connections between the schools
        
    }
}
