package New_Attempts_Java;
public class School{
    String name;
    int id;
    int matchupsLeft; 
    boolean currentMatchupsExhausted;
    String matchupNotes;

    public School(String name, int id){
        this.name = name;
        this.id = id;
        currentMatchupsExhausted = false;
        matchupsLeft = 2;
    }
    
    public void setCurrentMatchupsExhausted(boolean bool){
        currentMatchupsExhausted = bool;
    }
    public boolean getCurrentMatchupsExhausted(){
        return currentMatchupsExhausted;
    }
    public void decrementMatchupsLeft(){
        matchupsLeft--;
        if (matchupsLeft<0){
            matchupsLeft = 0;
        }
        if (matchupsLeft == 0){
            currentMatchupsExhausted = true;
        }
    }
    public void resetMatchupsLeft(){
        matchupsLeft = 2;
        currentMatchupsExhausted = false;
    }

    public String getName(){return name;}

    public int getId(){return id;}

    public String getMatchupNotes(){return matchupNotes;}
}