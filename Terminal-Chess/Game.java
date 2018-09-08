/**
 * Write a description of class Game here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Game
{
    public int[][] gameBoard;
    public Piece[][] piecesBoard;
    
    public boolean isWhiteTurn;
    
    /**
     * Constructor for objects of class Game
     */
    public Game(){
        Board board = new Board();
        gameBoard = board.generator();
        piecesBoard = new Piece[gameBoard.length][gameBoard.length];
    }
    
    public void newGame() {
        whiteStartPosition();
        blackStartPosition();
        
        isWhiteTurn = true;
        
        displayBoard();
    }
    
    public void displayBoard() {
        
        for(int x=0; x < gameBoard.length; x++){
            
            System.out.println("");
            for(int y=0; y < gameBoard[x].length; y++){
                
                Piece piece = piecesBoard[x][y];
                if(piece == null) {
                    System.out.print(" - ");
                } else {
                    
                    switch(piece.getType()) {
                        
                        case PAWN:
                            System.out.print(" P ");
                        break;
                    }
                }
            }
        }
    }
    
    /***
     * initialise white pieces position
     */
    private void whiteStartPosition() {
        
        for(int x=0; x < gameBoard.length; x++){
            for(int y=0; y < gameBoard[x].length; y++){
                
                if(x == 1) {
                    piecesBoard[x][y] = new PiecePawn();
                }
            }
        }
    }
    
    /***
     * initialise black pieces position
     */
    private void blackStartPosition(){
        
        for(int x=0; x < gameBoard.length; x++){
            for(int y=0; y < gameBoard[x].length; y++){
                
                if(x == (gameBoard.length - 2)) {
                    piecesBoard[x][y] = new PiecePawn();
                }
            }
        }
    }
    
    private boolean turn(int[][] currentPos, int[][] newPos) {
        
        if(isWhiteTurn) {
            // What to do
        }
        
        isWhiteTurn = !isWhiteTurn;
        
        return false;
    }
}
