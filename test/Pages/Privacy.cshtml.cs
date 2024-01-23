using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System;
using Newtonsoft.Json.Linq;

namespace test.Pages
{
    public class PrivacyModel : PageModel
    {
        private readonly IWebHostEnvironment _environment;
        private readonly ILogger<PrivacyModel> _logger;

        public PrivacyModel(IWebHostEnvironment environment, ILogger<PrivacyModel> logger)
        {
            _environment = environment;
            _logger = logger;
        }

        public List<ImageModel> Images { get; private set; }

        public void OnGet()
        {
            string folderPath = Path.Combine(_environment.WebRootPath, "images"); // Combine with the web root path
            Images = GetImagesFromFolder(folderPath);
        }

        private List<ImageModel> GetImagesFromFolder(string folderPath)
        {
            var images = new List<ImageModel>();

            if (Directory.Exists(folderPath))
            {
                var imageFiles = Directory.GetFiles(folderPath, "*.png"); // Change the extension as needed

                images.AddRange(imageFiles.Select(filePath =>
                {
                    var fileName = Path.GetFileName(filePath);
                    return new ImageModel { FileName = fileName };
                }));
            }

            return images;
        }
    }
}
