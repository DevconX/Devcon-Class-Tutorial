/**
 * Write a description of class Board here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Board
{
    private final static int DEFAULT_BOARD_SIZE = 8;
    
    /**
     * Generate default board
     */
    public int[][] generator() {
        return new int[DEFAULT_BOARD_SIZE][DEFAULT_BOARD_SIZE];
    }
}
