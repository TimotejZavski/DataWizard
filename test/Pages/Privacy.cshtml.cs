using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using System.IO;
using static System.Net.Mime.MediaTypeNames;
using static System.Runtime.InteropServices.JavaScript.JSType;


namespace test.Pages
{
    public class PrivacyModel : PageModel
    {
        public string[] ImageUrls { get; private set; }

        private readonly ILogger<PrivacyModel> _logger;

        public PrivacyModel(ILogger<PrivacyModel> logger)
        {
            _logger = logger;
        }

        public List<ImageModel> Images { get; private set; }

        public void OnGet()
        {
            string folderPath = "/Users/timzav/Desktop/test/test/wwwroot/p_images/"; // Change this to the path of your image folder
            Images = GetImagesFromFolder(folderPath);
        }

        private List<ImageModel> GetImagesFromFolder(string folderPath)
        {
            var images = new List<ImageModel>();

            if (Directory.Exists(folderPath))
            {
                var imageFiles = Directory.GetFiles(folderPath, "*.png"); // Change the extension as needed

                images.AddRange(imageFiles.Select(filePath => new ImageModel { FilePath = filePath }));


            }

            return images;
        }
    }
}
