/**
 * Write a description of class PiecePawn here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class PiecePawn implements Piece
{
    public MovementType movement() {
        return MovementType.STRAIGHT;
    }
    
    public boolean isOneDirection() {
        return true;
    }
    
    public boolean isUpgradable() {
        return true;
    }
    
    public ChessType getType() {
        return ChessType.PAWN;
    }
}
