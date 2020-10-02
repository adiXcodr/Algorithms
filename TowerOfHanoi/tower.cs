public class tower
    {
        public static void Main(String[] args)
        {
            char startRing = '1'; // start tower in output
            char endRing = '2'; // end tower in output
            char tempRing = '3'; // temporary tower in output
            int totalDisks = 3; // number of disks
 
            solveTowers(totalDisks, startRing, endRing, tempRing);
        }
 
        private static void solveTowers(int n, char startRing, char endRing, char tempRing)
        {
            if (n > 0)
            {
                solveTowers(n - 1, startRing, tempRing, endRing);
                Console.WriteLine("Move disk from " + startRing + ' ' + endRing);
                solveTowers(n - 1, tempRing, endRing, startRing);
 
            }
        }        
    }