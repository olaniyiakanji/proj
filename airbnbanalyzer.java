import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AirbnbAnalyzerMain {
    public static void main(String[] args) {
        AirbnbAnalyzer analyzer = new AirbnbAnalyzer(5);
        Scanner scanner = new Scanner(System.in);

        System.out.println("Airbnb Analyzer");
        System.out.println("Enter a listing (or 'q' to quit):");

        while (true) {
            String listing = scanner.nextLine().trim();
            if (listing.equalsIgnoreCase("q")) {
                break;
            }

            analyzer.addListing(listing);
        }

        System.out.println();
        System.out.println("Analyzing listings...");
        analyzer.analyze();
    }
}

class AirbnbAnalyzer {
    private int listingsPerSlide;
    private List<List<String>> slides;

    public AirbnbAnalyzer(int listingsPerSlide) {
        this.listingsPerSlide = listingsPerSlide;
        this.slides = new ArrayList<>();
        slides.add(new ArrayList<>());
    }

    public void addListing(String listing) {
        List<String> currentSlide = slides.get(slides.size() - 1);

        if (currentSlide.size() < listingsPerSlide) {
            currentSlide.add(listing);
        } else {
            List<String> newSlide = new ArrayList<>();
            newSlide.add(listing);
            slides.add(newSlide);
        }
    }

    public void analyze() {
        for (int i = 0; i < slides.size(); i++) {
            System.out.println("Slide " + (i + 1) + ":");
            for (String listing : slides.get(i)) {
                // Perform analysis on the listing
                System.out.println("Analyzing listing: " + listing);
            }
            System.out.println();
        }
    }
}
